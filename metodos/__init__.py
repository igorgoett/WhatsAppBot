# Import Libraries
import pywhatkit
import pyautogui
import time
from tkinter import *

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor
cont = 0
contatos = ['+5521997883456','+5521993232325', '+5521980362875']
nome_contato = ['Jenniffer', 'Felipe', 'Atila']
# print(screen_width, screen_height) # prints your monitor's resolution
while cont < len(contatos):
    msg = f"Bom dia Sr.(a) {nome_contato[cont]}\nMeu nome é Jenniffer, sou da Construtora Você, gostaria de saber se o Sr. (a) está tendo alguma dúvida em relação ao seu Financiamento Imobiliário? Possui aplicativo de Habitação Caixa? Está tendo alguma dificuldade no seu relacionamento com a CAIXA ECONÔMICA FEDERAL?\nE em relação as suas parcelas em aberto conosco, gostaria de verificar se o senhor (a) possui alguma previsão para pagamento?\nCaso já tenha realizado o pagamento, gentileza desconsiderar a mensagem acima.\nAtenciosamente\n\nRelacionamento com o Cliente\n"
    pywhatkit.sendwhatmsg_instantly(contatos[cont], msg) # Sends the message
    cont += 1
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.900) # Moves the cursor the the message bar in Whatsapp
    time.sleep(10)
    pyautogui.click() # Clicks the bar
    pyautogui.press('enter') # Sends the message
    time.sleep(10)
    pyautogui.hotkey('ctrl','w')
    time.sleep(10)
    pyautogui.press('enter') # Sends the message
