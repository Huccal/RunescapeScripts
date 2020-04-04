import pyautogui as pauto
import time
import random

from modules import RandomTime

def type_this(strings):
    """Types the passed characters with random pauses in between strokes"""
    for s in strings:
        # delay between key presses--key UP/DOWN
        #autopy.key.toggle(s, True)
        pauto.keyDown(s)
        time.sleep(RandomTime.randTime(0,0,0,0,0,5))
        pauto.keyUp(s)
        # delay after key UP--next key 

def press(button):
    pauto.keyDown(button)
    time.sleep(RandomTime.randTime(0, 0, 0, 0, 0, 5))
    pauto.keyUp(button)

def pressDef(button, secs):
    pauto.keyDown(button)
    time.sleep(secs)
    pauto.keyUp(button)