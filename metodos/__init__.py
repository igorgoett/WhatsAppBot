# Import Libraries
import pywhatkit
import pyautogui
import time
from tkinter import *
from contacts import first_names, new_phones
import msg

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor
cont = 0


while cont < len(first_names):

    pywhatkit.sendwhatmsg_instantly(new_phones[cont], msg.msg(first_names,cont)) # Sends the message
    cont += 1
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.900) # Moves the cursor the the message bar in Whatsapp || CHANGE HEIGHT ACCORDING
    time.sleep(5)
    pyautogui.click() # Clicks the bar
    pyautogui.press('enter') # Sends the message
    time.sleep(5)
    pyautogui.hotkey('ctrl','w')
    time.sleep(5)
    pyautogui.press('enter') # Sends the message
