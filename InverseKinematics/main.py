import threading
from time import sleep
from X_Scaler import get_x_value, start_x_updates
from Y_Scaler import get_y_value, start_y_updates

exit_program = False

def main():
    global exit_program

    try:
        x_update_thread = threading.Thread(target=start_x_updates, daemon=True)
        y_update_thread = threading.Thread(target=start_y_updates, daemon=True)
        x_update_thread.start()
        y_update_thread.start()
        while not exit_program:
            x_val = get_x_value()
            y_val = get_y_value()
            last_x = x_val
            last_y = y_val
            print(f"(X: {x_val}, Y: {y_val})")
            last_x = x_val
            last_y = y_val
            sleep(0.01)

    except KeyboardInterrupt:
        print("Exiting program...")
        exit_program = True

    finally:
        print("Program exited.")

if __name__ == "__main__":
    main()
