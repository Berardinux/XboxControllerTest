import evdev
from time import sleep
import threading
import numpy as np

Y = 511
current_value = 32768
exit_program = False
DEAD_ZONE = 1023
device_path = '/dev/input/event25'

def update_y():
    global Y, current_value, exit_program
    last_y = Y
    while not exit_program:
        if abs(current_value - 32768) > DEAD_ZONE:
            if current_value > 42768:
                if current_value > 60535:
                    Y -= 8
                elif current_value > 51652:
                    Y -= 4
                else:
                    Y -= 1
            elif current_value < 22768:
                if current_value < 5000:
                    Y += 8
                elif current_value < 13883:
                    Y += 4
                else:
                    Y += 1

        Y = max(0, min(Y, 1023))
        last_y = Y
        sleep(0.05)

def get_y_value():
    y_coordinates = np.interp(Y, [0, 1023], [0, 500])
    return round(y_coordinates)

def start_y_updates():
    global exit_program, current_value
    device = evdev.InputDevice(device_path)
    print(device)

    y_thread = threading.Thread(target=update_y, daemon=True)
    y_thread.start()

    try:
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_ABS:
                if event.code == evdev.ecodes.ABS_RZ:
                    current_value = event.value

            sleep(0.001)

    except KeyboardInterrupt:
        pass
    finally:
        exit_program = True
        y_thread.join()
        print("Program exited.")
