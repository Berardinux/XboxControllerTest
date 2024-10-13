import evdev
from time import sleep

device = evdev.InputDevice('/dev/input/event18')
print(device)

Z = 50

try:
  for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
      if event.code == evdev.ecodes.ABS_Y:
        
        if event.value > 34768: # Middle of analog stick is 32768 Max is 65535
          Z += 1
        elif event.value < 30768:
          Z -= 1
        
        Z = max(0, min(Z, 1000))
        print(event.value)
        print(f"Current Z: {Z}")

except KeyboardInterrupt:
  pass
finally:
  exit 