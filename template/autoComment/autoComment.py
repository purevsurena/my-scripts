import pyautogui
import time

comments = ["Scripted"]

time.sleep(5)

for i in range(1000):
  pyautogui.typewrite(comments[0])
  pyautogui.typewrite("\n")
  time.sleep(2)