import evdev
from time import sleep
import threading

# Open the event file for your input device (change to your specific event number)
device = evdev.InputDevice('/dev/input/event25')  # Replace with your specific event file
print(device)

Y = 500
current_value = 32768  # Current analog stick position
exit_program = False   # Flag to exit the program gracefully

# Define a dead zone for the analog stick
DEAD_ZONE = 1000

def update_y():
    """Continuously adjust Y based on the analog stick value."""
    global Y, current_value, exit_program
    last_y = Y  # Track the last value of Y for printing

    while not exit_program:
        # Skip updates if the stick is in the dead zone
        if abs(current_value - 32768) > DEAD_ZONE:
            if current_value > 42768:  # Stick pulled backward
                if current_value > 60535:  # Fast speed
                    Y -= 7
                elif current_value > 51652:  # Medium speed
                    Y -= 3
                else:  # Slow speed
                    Y -= 1
            elif current_value < 22768:  # Stick pushed forward
                if current_value < 5000:  # Fast speed
                    Y += 7
                elif current_value < 13883:  # Medium speed
                    Y += 3  # Fix: Correct decrement
                else:  # Slow speed
                    Y += 1

        # Keep Y within bounds
        Y = max(0, min(Y, 1000))

        # Print Y only when it changes
        if Y != last_y:
            print(f"Current Y: {Y}")
            last_y = Y

        # Adjust update speed
        sleep(0.05)  # Adjust as needed for smoother response

# Start the thread for updating Y
y_thread = threading.Thread(target=update_y)
y_thread.daemon = True  # Ensures thread exits with the main program
y_thread.start()

try:
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            if event.code == evdev.ecodes.ABS_RZ:  # Change here to read the right stick
                current_value = event.value  # Directly update the value

        sleep(0.001)  # Short delay to avoid high CPU usage

except KeyboardInterrupt:
    pass
finally:
    exit_program = True  # Signal the thread to stop
    y_thread.join()  # Wait for the thread to finish
    print("Program exited.")
