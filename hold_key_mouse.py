from pynput.mouse import Controller as Controller_mouse
from pynput.mouse import Button
from pynput.keyboard import Controller as Controller_keyboard
from pynput.keyboard import Key
from time import sleep

mouse = Controller_mouse()
keyboard = Controller_keyboard()

mouse_button_pressed = None
key_pressed = None
waiting_time = 5

if __name__ == '__main__':
    try:
        mouse_button_choice = input("0 for left click, 1 for right click\n")
        key_choice = input("What key do you want to be pressed?\nOptions:\n\t- space: y\n")
        delay = 0.5
        if mouse_button_choice == "0":
            mouse_button_pressed = Button.left
        elif mouse_button_choice == "1":
            mouse_button_pressed = Button.right

        if key_choice == "y":
            key_pressed = Key.space
        print(f"Waiting {waiting_time} seconds for you so you can change the window")
        sleep(waiting_time)
        print("Starting...")
        while True:
            if mouse_button_pressed is not None:
                mouse.press(mouse_button_pressed)
            if key_pressed is not None:
                keyboard.press(key_pressed)
            # pause 1 second, because in minecraft it doesn't look that nice xD
            sleep(1)

    except KeyboardInterrupt:
        if mouse_button_pressed is not None:
            mouse.release(mouse_button_pressed)
        if key_pressed is not None:
            keyboard.release(key_pressed)
        print("\nUser aborted. Stopping...")
        exit()
