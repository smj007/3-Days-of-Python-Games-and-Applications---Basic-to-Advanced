# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:29:30 2020

@author: saimi
"""
import pyautogui
pyautogui.click()
dist = 200 #Set according to size of spiral

while dist > 0:
    print(dist, 0)
    pyautogui.dragRel(dist, 0, duration = 0.1) #RIGHT
    dist = dist - 25
    print(0, dist)
    pyautogui.dragRel(0, dist, duration = 0.1)  #DOWN
    dist = dist - 25
    print(-dist, 0)
    pyautogui.dragRel(-dist, 0, duration = 0.1) #LEFT
    dist = dist - 25
    print(0, -dist)
    pyautogui.dragRel(0, -dist, duration = 0.1)  #UP
    
    #Modify the values according to what you wish to draw
    #Use MS Paint and place the mouse pointer from where we wish to draw
      
    
    


