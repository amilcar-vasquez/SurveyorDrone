# Tello SDK — Command Reference (v1.3)

> Connect via WiFi UDP to Tello at `192.168.10.1:8889`  
> Send `command` first to enter SDK mode, then issue other commands. :contentReference[oaicite:0]{index=0}  
> Responses: `"ok"` for success, `"error"` (or other code) otherwise. :contentReference[oaicite:1]{index=1}  

---

## 1. Control Commands (no “?” or additional parameter)

| Command        | Description                             | Notes / Valid Values                         |
|----------------|-----------------------------------------|----------------------------------------------|
| `command`      | Enter SDK mode                           | Must be sent before other commands :contentReference[oaicite:2]{index=2} |
| `takeoff`      | Drone automatically takes off            | — :contentReference[oaicite:3]{index=3} |
| `land`         | Drone automatically lands                | — :contentReference[oaicite:4]{index=4} |
| `streamon`     | Start video streaming                    | — :contentReference[oaicite:5]{index=5} |
| `streamoff`    | Stop video streaming                     | — :contentReference[oaicite:6]{index=6} |
| `emergency`    | Stop all motors immediately              | Use in emergencies only :contentReference[oaicite:7]{index=7} |
| `up x`         | Fly upward by x cm                       | x = 20–500 :contentReference[oaicite:8]{index=8} |
| `down x`       | Fly downward by x cm                     | x = 20–500 :contentReference[oaicite:9]{index=9} |
| `left x`       | Fly left by x cm                         | x = 20–500 :contentReference[oaicite:10]{index=10} |
| `right x`      | Fly right by x cm                        | x = 20–500 :contentReference[oaicite:11]{index=11} |
| `forward x`    | Fly forward by x cm                      | x = 20–500 :contentReference[oaicite:12]{index=12} |
| `back x`       | Fly backward by x cm                     | x = 20–500 :contentReference[oaicite:13]{index=13} |
| `cw x`         | Rotate clockwise by x degrees            | x = 1–3600 :contentReference[oaicite:14]{index=14} |
| `ccw x`        | Rotate counter-clockwise by x degrees    | x = 1–3600 :contentReference[oaicite:15]{index=15} |
| `flip x`       | Flip in a direction                     | x ∈ {`l`, `r`, `f`, `b`} :contentReference[oaicite:16]{index=16} |
| `go x y z speed` | Fly to absolute coordinate (x,y,z) at speed | x,y,z = 20–500; speed = 10–100 :contentReference[oaicite:17]{index=17} |
| `curve x1 y1 z1 x2 y2 z2 speed` | Fly along a curve through two points | Intermediate constraints apply; speed = 10–60 :contentReference[oaicite:18]{index=18} |

---

## 2. Set Commands (modify settings)

| Command            | Description                         | Valid Range / Notes                        |
|--------------------|-------------------------------------|---------------------------------------------|
| `speed x`          | Set movement speed                  | x = 10–100 :contentReference[oaicite:19]{index=19} |
| `rc a b c d`       | Manual RC-style control             | a,b,c,d each in –100..100 :contentReference[oaicite:20]{index=20} |
| `wifi ssid pass`   | Set WiFi SSID and password           | — :contentReference[oaicite:21]{index=21} |

---

## 3. Read Commands (with `?` — query state)

| Command       | Description / Return                     |
|----------------|------------------------------------------|
| `speed?`       | Returns current speed (cm/s) :contentReference[oaicite:22]{index=22} |
| `battery?`     | Returns remaining battery (%) :contentReference[oaicite:23]{index=23} |
| `time?`        | Returns elapsed flight time (s) :contentReference[oaicite:24]{index=24} |
| `height?`      | Returns current height (cm) :contentReference[oaicite:25]{index=25} |
| `temp?`        | Returns internal temperature (°C) :contentReference[oaicite:26]{index=26} |
| `attitude?`    | Returns pitch, roll, yaw :contentReference[oaicite:27]{index=27} |
| `baro?`        | Returns barometer reading (m) :contentReference[oaicite:28]{index=28} |
| `acceleration?`| Returns x, y, z acceleration (0.001 g) :contentReference[oaicite:29]{index=29} |
| `tof?`          | Returns distance from TOF sensor (cm) :contentReference[oaicite:30]{index=30} |
| `wifi?`         | Returns WiFi SNR (signal-to-noise ratio) :contentReference[oaicite:31]{index=31} |

---

## 4. State Format & Safety Notes

- Tello periodically sends state info (if SDK mode active) as a string:

