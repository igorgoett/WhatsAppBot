
#MUDAR NAMES E INDEX DE ACORDO COM A NECESSIDADE
def msg(names, index):
    text = f"Bom dia Sr.(a) {names[index]}\nMeu nome é XXXXXX, sou da XXXXXXXXXX, gostaria de saber se o Sr. (a) está tendo alguma dúvida em relação ao seu XXXXXXXXXXXXXXXXX? Possui aplicativo de XXXXXXXXXXX? Está tendo alguma dificuldade no seu relacionamento com a XXXXXXXXXXXXXX?\nE em relação as suas parcelas em aberto conosco, gostaria de verificar se o senhor (a) possui alguma previsão para pagamento?\nCaso já tenha realizado o pagamento, gentileza desconsiderar a mensagem acima.\nAtenciosamente\n\nRelacionamento com o Cliente\n"
    return text


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