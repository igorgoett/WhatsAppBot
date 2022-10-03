from datetime import datetime


def opcao_msg(names, index,opcao,nome_atendimento):
    adimplente = f"{time} Sr.(a) {names[index]}\nMeu nome é {nome_atendimento}, sou da Construtora Você, o motivo da mensagem é para saber se o (a) Sr. (a) está tendo alguma dúvida em relação ao seu Financiamento Imobiliário?\nPossui aplicativo de Habitação Caixa?\nEstá tendo alguma dificuldade no seu relacionamento com a CAIXA ECONÔMICA FEDERAL?"

    inadimplente = f"{time} Sr.(a) {names[index]}\nMeu nome é {nome_atendimento}, sou da Construtora Você, gostaria de saber se o Sr. (a) está tendo alguma dúvida em relação ao seu Financiamento Imobiliário? Possui aplicativo de Habitação Caixa? Está tendo alguma dificuldade no seu relacionamento com a CAIXA ECONÔMICA FEDERAL?\nE em relação as suas parcelas em aberto conosco, gostaria de verificar se o senhor (a) possui alguma previsão para pagamento?\nCaso já tenha realizado o pagamento, gentileza desconsiderar a mensagem acima."

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