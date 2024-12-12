import evdev
from time import sleep
import threading
import numpy as np

X = 511
current_value = 32768
exit_program = False
DEAD_ZONE = 1023
device_path = '/dev/input/event25'

def update_x():
    global X, current_value, exit_program
    last_x = X
    while not exit_program:
        if abs(current_value - 32768) > DEAD_ZONE:
            if current_value > 42768:
                if current_value > 60535:
                    X -= 8
                elif current_value > 51652:
                    X -= 4
                else:
                    X -= 1
            elif current_value < 22768:
                if current_value < 5000:
                    X += 8
                elif current_value < 13883:
                    X += 4
                else:
                    X += 1

        X = max(0, min(X, 1023))
        last_x = X
        sleep(0.05)

def get_x_value():
    x_coordinates = np.interp(X, [0, 1023], [0, 500])
    return round(x_coordinates)

def start_x_updates():
    """Call this from main.py to start reading device input and updating X."""
    global exit_program, current_value
    device = evdev.InputDevice(device_path)
    print(device)

    x_thread = threading.Thread(target=update_x, daemon=True)
    x_thread.start()

    try:
        for event in device.read_loop():
            if exit_program:
                break
            if event.type == evdev.ecodes.EV_ABS and event.code == evdev.ecodes.ABS_Y:
                current_value = event.value
            sleep(0.001)
    except KeyboardInterrupt:
        pass
    finally:
        exit_program = True
        x_thread.join()
        print("X update thread stopped.")
