#!/usr/bin/env python3
"""
Simple TLW004/Tello-style SDK script:
 - Enter SDK mode ("command")
 - Take off ("takeoff")
 - Hover for N seconds
 - Land ("land")

Assumes a Tello-like UDP SDK interface at 192.168.10.1:8889.
Adjust host/port if your TLW004 uses different endpoints.
"""

from __future__ import annotations

import argparse
import socket
import sys
import time
from typing import Tuple


def send_command(
	sock: socket.socket,
	addr: Tuple[str, int],
	cmd: str,
	*,
	timeout: float = 5.0,
	retries: int = 2,
) -> Tuple[bool, str]:
	"""Send a single SDK command and wait for a response.

	Returns (success, response_text).
	"""
	sock.settimeout(timeout)
	last_err = ""
	for attempt in range(retries + 1):
		try:
			sock.sendto(cmd.encode("utf-8"), addr)
			data, _ = sock.recvfrom(1024)
			resp = data.decode("utf-8", errors="ignore").strip().lower()
			ok = resp == "ok"
			return ok, resp
		except socket.timeout:
			last_err = "timeout"
		except OSError as e:
			last_err = str(e)
			# brief backoff on socket errors
			time.sleep(0.1)
		# retry after brief delay
		time.sleep(0.2)
	return False, last_err or "no response"


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description="TLW004 takeoff, hover, land script")
	parser.add_argument("--host", default="192.168.10.1", help="Drone SDK host (default: 192.168.10.1)")
	parser.add_argument("--port", type=int, default=8889, help="Drone SDK UDP port (default: 8889)")
	parser.add_argument(
		"--local-port",
		type=int,
		default=9000,
		help="Local UDP port to bind for responses (default: 9000)",
	)
	parser.add_argument(
		"--hover",
		type=float,
		default=5.0,
		help="Seconds to hover before landing (default: 5.0)",
	)
	args = parser.parse_args(argv)

	addr = (args.host, args.port)

	# Create UDP socket and bind to local port to receive responses.
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		sock.bind(("", args.local_port))
	except OSError as e:
		print(f"Failed to bind local UDP port {args.local_port}: {e}", file=sys.stderr)
		return 2

	print(f"Connecting to drone at {addr[0]}:{addr[1]} (local port {args.local_port})")
	try:
		# Enter SDK mode
		ok, resp = send_command(sock, addr, "command")
		print(f"-> command | <- {resp}")
		if not ok:
			print("Failed to enter SDK mode. Aborting.", file=sys.stderr)
			return 1

		# Takeoff
		ok, resp = send_command(sock, addr, "takeoff", timeout=10.0, retries=3)
		print(f"-> takeoff | <- {resp}")
		if not ok:
			print("Takeoff failed. Aborting.", file=sys.stderr)
			return 1

		# Hover for the requested duration
		hover_s = max(0.0, float(args.hover))
		print(f"Hovering for {hover_s:.1f}s…")
		time.sleep(hover_s)

		# Land
		ok, resp = send_command(sock, addr, "land", timeout=10.0, retries=3)
		print(f"-> land | <- {resp}")
		if not ok:
			print("Land command reported failure.", file=sys.stderr)
			return 1

		print("Sequence complete.")
		return 0
	except KeyboardInterrupt:
		# Attempt a safe land on Ctrl+C
		try:
			print("\nInterrupted. Attempting to land…")
			send_command(sock, addr, "land", timeout=5.0, retries=1)
		except Exception:
			pass
		return 130
	finally:
		sock.close()


if __name__ == "__main__":
	raise SystemExit(main())

