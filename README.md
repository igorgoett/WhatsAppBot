# WhatsAppBot
Programa para mandar mensagens automaticas diretamente para o contato.

Primeiro passo seria incluir um arquivo em excel na pasta do programa, alterar o nome do arquivo para contato.xlsx.

O programa pegará 2 colunas para alimentar as informações, 1 coluna com a primeira linha chamada 'Nomes' e a segunda como 'Contato' (pode ser alterado no arquivo contacts.py). Deixei um arquivo excel já formatado com o nome de contatos_sample.xlsx pode ser alterado para facilitar, basta remover o "_sample.xlsx"

A mensagem fica no arquivo msg.py, deixei um arquivo já configurado como msg_sample.py, basta fazer as alterações necessárias na mensagem.

Outra alteração que pode ser feito é no arquivo principal __init__.py, na função ```time.sleep(5)``` pode ser alterado o valor dependendo do desempenho do computador / internet.

Eu fiz esse programa com a intenção de facilitar uma atividade do meu trabalho atual. 

Espero que possa ser útil para outros.