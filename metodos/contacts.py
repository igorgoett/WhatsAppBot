from tkinter.font import names
import pandas as pd

excel_file = 'contatos.xlsx'
df = pd.read_excel(excel_file)

Names = list(df.Nomes)
raw_phones = list(df.Contato)
new_phones = []

for num in raw_phones:
    new_phones.append('+55'+num.replace(' ','').replace('-','').replace('(','').replace(')',''))
    
print(new_phones)