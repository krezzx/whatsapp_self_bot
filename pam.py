import pyautogui as p
import time
import tkinter as tk


#keep chrome at 2nd from left
#whatsapp web size 90%
#and it works fine

name=input("Enter Name")
msg=input("Enter YOur Message")
time.sleep(3)
p.moveTo(194,8)
p.click()
p.moveTo(144,44)
p.click()

p.moveTo(177,221)
p.click()
p.write(name)
time.sleep(3)
p.moveTo(154,332)
p.click()
p.click()

time.sleep(1)

p.write(msg)
p.press("enter")







    
