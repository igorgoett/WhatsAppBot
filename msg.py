from datetime import datetime


def opcao_msg(names, index,opcao,nome_atendimento):
    adimplente = f"{time} Sr.(a) {names[index]}\nMeu nome é {nome_atendimento}, "

    inadimplente = f"{time} Sr.(a) {names[index]}\nMeu nome é {nome_atendimento}, 

    if opcao == '1':
        text = inadimplente
    elif opcao == '2':
        text = adimplente

    return text



now = datetime.now()

current_time = now.strftime("%H:%M:%S")

if current_time < "12:00":
    time = 'Bom dia'
elif current_time > "12:00":
    time = 'Boa tarde'
