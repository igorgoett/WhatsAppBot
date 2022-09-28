from datetime import datetime

#MUDAR NAMES E INDEX DE ACORDO COM A NECESSIDADE
def msg(names, index):
    text = f"{time} Sr.(a) {names[index]}\nMeu nome é XXXXX, sou da XXXXXXXXXXX, gostaria de saber se o Sr. (a) está tendo alguma dúvida em relação ao seu XXXXXXXXXXXXXXXXXX? Possui aplicativo de XXXXXXXXXXXXXXXXXXXX? Está tendo alguma dificuldade no seu relacionamento com a XXXXXXXXXXXXXXXXXXXX?\nE em relação as suas parcelas em aberto conosco, gostaria de verificar se o senhor (a) possui alguma previsão para pagamento?\nCaso já tenha realizado o pagamento, gentileza desconsiderar a mensagem acima."
    return text


now = datetime.now()

current_time = now.strftime("%H:%M:%S")

if current_time < "12:00":
    time = 'Bom dia'
elif current_time > "12:00":
    time = 'Boa tarde'

#TESTS
# cont = 0
# first_names=["Guilherme",
#             "Henrique",
#             "Aline",
#             "Gustavo",
#             ]

# while cont < len(first_names):
#     print(msg(first_names,cont))
#     cont += 1