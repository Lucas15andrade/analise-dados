import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('autos.csv')
#migracao = pd.read_csv('migracao-janeiro-2019.csv')

print(data.head())

#Quantidade de linhas de cada atributo
print(data.count())

#Quantidade de colunas do DataFrame
print(len(data.columns))

#Máximo e Mínimo de cada coluna
print(data.max())
print(data.min())

#Valores faltosos
#Coluna
print(data.isna().sum(axis=0))
#Linha
print(data.isna().sum(axis=1))

#Correlação entre os atributos da base
#Retorna uma tabela apenas com dados numéricos mostrando a correlação entre todos os atributos.
print(data.corr())

#Criando dataframe auxiliar
dataAux = data.copy()
#Removendo colunas não numericas
dataAux.drop(columns=['normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
                    'engine-type', 'num-of-cylinders', 'fuel-system', 'bore', 'stroke', 'horsepower', 'peak-rpm',
                    'price'], inplace=True)
print(data.info())
#printando e alterando no DF com o inplace
#Substituindo valores faltosos pela média
print(dataAux.fillna(value=data.mean(), inplace=True))

#Normalizando dados
dataNorm = (dataAux - dataAux.min())/(dataAux.max() - dataAux.min())

print(dataNorm.head())
print(data.head())

#Informações
data1 = data[data['make'] == 'alfa-romero']
data2 = data[data['fuel-type'] == 'gas']
data3 = data[(data['body-style'] == 'sedan') & (data['num-of-doors'] == 'four')]
data4 = data[(data['make'] == 'volkswagen') & (data['fuel-type'] == 'diesel')]
data5 = data[(data['make'] == 'volvo') & (data['fuel-type'] == 'diesel')]

data1['make'].value_counts().plot.bar(title='Carros da marca Alfa Romero')
plt.show()

data2['make'].value_counts().plot.bar(title='Carros com combustível a gás')
plt.show()

data3['make'].value_counts().plot.bar(title='Carros sedan e com 4 portas')
plt.show()

data4['make'].value_counts().plot.bar(title='Carros da Volkswagen e a diesel')
plt.show()

data5['make'].value_counts().plot.bar(title='Carros da volvo e a diesel')
plt.show()

