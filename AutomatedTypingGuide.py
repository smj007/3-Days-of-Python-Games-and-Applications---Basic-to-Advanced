# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:05:58 2020

@author: saimi
"""

#Function to type
import pyautogui

pyautogui.click(100, 100) #Set the position of the cursor to type

pyautogui.typewrite("Hello world") #At fast speed
pyautogui.typewrite("Hello world", interval = 0.2) #At a human-like speed
pyautogui.click(100, 100); pyautogui.typewrite(["a", "b", "left", "left", "X", "Y"])
#Above prints XYab - Use case of other keys
#Passing a list to typewrite helps to type non alpha keys like shift, left etc

#To view all the keys commands
pyautogui.KEYBOARD_KEYS

#To just press a single key
pyautogui.press('f1')

#TO press 2 keys at the same time
pyautogui.hotkey('ctrl', 'o') #Keyboard shortcuts can be used
