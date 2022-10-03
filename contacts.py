import pandas as pd

excel_file = 'contatos.xlsx'
df = pd.read_excel(excel_file)

raw_names = list(df.Nomes)
raw_phones = list(df.Contato)
first_names = []
new_phones = []

#formatando nomes
for nomes in raw_names:
    nomes = nomes.split()[0]
    first_names.append(nomes)

#formatando números
for num in raw_phones:
    num = str(num)
    new_phones.append('+55'+num.replace(' ','').replace('-','').replace('(','').replace(')',''))
    
print(first_names, new_phones)