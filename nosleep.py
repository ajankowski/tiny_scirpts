# nosleep script to prevent the computer from going to sleep
# libraty used https://pyautogui.readthedocs.io/en/latest/quickstart.html 

import pyautogui
from time import sleep

pyautogui.FAILSAFE = True #

i = 0

screen = pyautogui.size()
print(screen)

while True:

    if i == 0:
        print('start')
    pyautogui.moveTo(int(screen[0]/2), int(screen[1]/2), duration=10)
    sleep(10)
    pyautogui.moveTo(int(screen[0]/3), int(screen[1]/3), duration=10)  
    sleep(10)
    i += 1
    print('sekundy:', i*40, 'pozycja myszki: ', pyautogui.position())

   
