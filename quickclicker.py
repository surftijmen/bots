#random code for fenetre

import pyautogui # # #
import time
from keyboard import press

print("Hello World")

delay = 60

times = 5
x = pyautogui.position()

while times > 0:
    time.sleep(1)
    times -= 1
    if times == 0:
       # pyautogui.click(1500, 500) #connect
       # time.sleep(30)

        pyautogui.moveTo(268, 92)
        pyautogui.click(268, 92) #screen
      #  press('enter')
        times = delay
        time.sleep(5)
        pyautogui.click()

    if pyautogui.position() != x:
        times = delay

    x = pyautogui.position()


delay2 = 310
time2 = 5

# while time2 > 0:
#     time.sleep(1)
#     time2 -= 1
#     if time2 == 0:
#        # pyautogui.click(1500, 500) #connect
#        # time.sleep(30)

#         pyautogui.hotkey('ctrl', 'r')
#         time.sleep(3)

#         pyautogui.moveTo(1500, 500)
#         pyautogui.click(1500, 500) #screen
#       #  press('enter')
#         time2 = delay
#         time.sleep(30)
#         pyautogui.press('left')
#         time.sleep(1)
#         pyautogui.press('enter')


#     if pyautogui.position() != x:
#         time2 = delay

#     x = pyautogui.position()