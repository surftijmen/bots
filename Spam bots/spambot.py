import pyautogui, time

startDelay = 5
messageDelay = 0.5
fileName = "Spam bots/spam.txt"

time.sleep(startDelay)

f = open(fileName, 'r')

for word in f:
    if (word != "\n"):
        
        pyautogui.typewrite(word)
        pyautogui.press("enter")

        print(word)
        time.sleep(messageDelay)