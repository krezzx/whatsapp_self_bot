import pyautogui as p
import time as t

t.sleep(4)
x,y=p.position()
f=open("pos.txt","a")
f.write(str(x)+" ")
f.write(str(y))
f.close()
