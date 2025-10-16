Where fields represent: pitch, roll, yaw, velocities, temps, distance, height, battery, barometer, time, accelerometer axes. :contentReference[oaicite:32]{index=32}

- Safety: if Tello does not receive **any** command for **15 seconds**, it will auto-land. :contentReference[oaicite:33]{index=33}  
- To reset WiFi settings: long-press the drone for 5 seconds while it’s powered on. The indicator LED turns off then flashes yellow; WiFi resets to factory defaults (no password). :contentReference[oaicite:34]{index=34}  

---

## 5. Example Usage Sequence (in pseudo code)

```text
send("command")
expect("ok")

send("takeoff")
expect("ok")

send("up 50")
expect("ok")

send("cw 90")
expect("ok")

send("forward 100")
expect("ok")

send("land")
expect("ok")
