# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:28:15 2020

@author: saimi
"""

import pyautogui

pyautogui.screenshot() #command to take a screenshot

pyautogui.screenshot("path") #Path with the filename to store the ss to

pyautogui.locateOnScreen("saved-img_path") #locates the item on the screen as per the img
#Returns x, y, height and width
#This function needs exact matching of all the pixel data between the img and screen item
#No window should block, and also hinder it slightly, else the detection will fail

pyautogui.locateCenterOnScreen("saved-img_path") 
#returns only x, y coordinates of the center of the object

#Combine the keyboard, mouse and screenshot functions and use - 
#CHECKOUT THE SUSHI GAME (try using pyautogui and image recognition)