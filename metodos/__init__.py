# Import Libraries
import pywhatkit
import pyautogui
import time
from tkinter import *
from contacts import first_names, new_phones

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor
cont = 0


while cont < len(first_names):
    msg = f"Bom dia Sr.(a) {first_names[cont]}\nMeu nome é Jenniffer, sou da Construtora Você, gostaria de saber se o Sr. (a) está tendo alguma dúvida em relação ao seu Financiamento Imobiliário? Possui aplicativo de Habitação Caixa? Está tendo alguma dificuldade no seu relacionamento com a CAIXA ECONÔMICA FEDERAL?\nE em relação as suas parcelas em aberto conosco, gostaria de verificar se o senhor (a) possui alguma previsão para pagamento?\nCaso já tenha realizado o pagamento, gentileza desconsiderar a mensagem acima.\nAtenciosamente\n\nRelacionamento com o Cliente\n"

    pywhatkit.sendwhatmsg_instantly(new_phones[cont], msg) # Sends the message
    cont += 1
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.900) # Moves the cursor the the message bar in Whatsapp || CHANGE HEIGHT ACCORDING
    time.sleep(5)
    pyautogui.click() # Clicks the bar
    pyautogui.press('enter') # Sends the message
    time.sleep(5)
    pyautogui.hotkey('ctrl','w')
    time.sleep(5)
    pyautogui.press('enter') # Sends the message
