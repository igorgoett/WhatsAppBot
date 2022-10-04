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

opcao = input(str('Qual tipo de cliente? \n1 - Inadimplente\n2 - Adimplente\n3 - Para Sair\nOpção:  '))
if opcao == '3':
    quit()
nome_atendimento = input(str('Nome do Atendente que vai aparecer na mensagem? '))
#tempo_mensagem = input(str('Quanto tempo de uma mensagem para outra [REPOSTA EM SEGUNDOS]: '))

while cont < len(first_names):
    pywhatkit.sendwhatmsg_instantly(new_phones[cont], msg.opcao_msg(first_names,cont,opcao,nome_atendimento)) # Sends the message
    cont += 1
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.900) # Moves the cursor the the message bar in Whatsapp || CHANGE HEIGHT ACCORDING
    time.sleep(3)
    pyautogui.click() # Clicks the bar
    pyautogui.press('enter') # Sends the message
    pyautogui.hotkey('ctrl','w') #close window
    pyautogui.press('enter') # close window

print('-'*30)
print('MENSAGENS ENVIADAS COM SUCESSO!')
print('-'*30)
time.sleep(2)
