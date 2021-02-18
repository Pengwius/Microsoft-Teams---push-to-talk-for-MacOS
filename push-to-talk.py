import pyautogui
import time
from pynput import keyboard

def on_press(key):
    print(key)
    key_pressed = None
    try:
        key_pressed = key.char
    except:
        print("No key")

    if key_pressed == ('p'):
        pyautogui.keyDown('command')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('m')
        pyautogui.keyUp('command')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('m')
        key_pressed = None
    

def on_release(key):
    print(key)
    key_pressed = None
    try:
        key_pressed = key.char
    except:
        print("No key")

    if key_pressed == ('p'):
        pyautogui.keyDown('command')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('m')
        pyautogui.keyUp('command')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('m')
        key_pressed = None

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()