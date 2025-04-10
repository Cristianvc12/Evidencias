import pandas as pd
banco = pd.read_csv('bank.csv')
print(banco.columns)
print(banco['job'])
banco["mora"]='nueva columna agregada'
print(banco.columns)
banco=banco.drop('mora',axis=1)
print(banco.columns)
cuatrocols = banco.iloc[:,:4]
print(cuatrocols)