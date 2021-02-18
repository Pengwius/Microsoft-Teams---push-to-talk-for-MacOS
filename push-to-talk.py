import pyautogui
from pynput import keyboard

def on_press(key):
    print(key)
    try: 
        if key.char == ('p'):
            print("dupa")
            pyautogui.keyDown('command')
            pyautogui.keyDown('shift')
            pyautogui.keyDown('m')
            pyautogui.keyUp('command')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('m')
    except:
        print("No key")

def on_release(key):
    print(key)
    try:
        if key.char == ('p'):
            print("dupa")
            pyautogui.keyDown('command')
            pyautogui.keyDown('shift')
            pyautogui.keyDown('m')
            pyautogui.keyUp('command')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('m')
    except:
        print("No key")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()