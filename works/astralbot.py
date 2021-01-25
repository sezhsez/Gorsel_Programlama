import pyautogui
import keyboard
import time


time.sleep(0.5)
ct = 1
#
# # COORDINATES
#     # Button 1 (x=159, y=958)
#     # Button 2 (x=294, y=956)
#     # Button 3 (x=426, y=956)
#     # Button 4 (x=562, y=959)
#     # Button 5 (x=703, y=957)
#     # Sell (x=656, y=883)
#     # Synthesize (x=432, y=880)



for i in range(100000):
    if keyboard.is_pressed('q'):
        print("q is pressed")
        break


    # Button 1
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)

    #Button 2
    pyautogui.click(x=602, y=880)

    # Button 1
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)
    pyautogui.click(x=359, y=880)

    #Button 2
    pyautogui.click(x=602, y=880)

    #Button 3
    pyautogui.click(x=850, y=880)

    #Button 4
    pyautogui.click(x=1094, y=880)

    #Button 5
    pyautogui.click(x=1356, y=880)

    #Sell
    pyautogui.click(x=1270, y=736)
    time.sleep(0.5)

    #Confirm
    pyautogui.click(x=1259, y=682)

    #Synthesize
    pyautogui.click(x=870, y=740)
