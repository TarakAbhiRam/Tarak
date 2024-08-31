from pyautogui import *
import pyautogui as p
import time as t
import keyboard
import random 
import win32api as win, win32con

tile1=(708,550)
tile2=(885,550)
tile3=(1033,550)
tile4=(1196,550)
#url == https://www.agame.com/game/magic-piano-tiles
def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    t.sleep(0.1)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    if keyboard.is_pressed('s'):  # Start
        while True:
            if p.pixel(708,550)[0] == 0:
                click(708,550)
            if p.pixel(885,550)[0] == 0:
                click(885,550)
            if p.pixel(1033,550)[0] == 0:
                click(1033,550)
            if p.pixel(1196,550)[0] == 0:
                click(1196,550)
            if keyboard.is_pressed('q'):  # Stop
                break
    t.sleep(0.1)  # Avoid high CPU usage

