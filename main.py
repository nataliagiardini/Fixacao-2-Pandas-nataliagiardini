import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('campeonato-brasileiro-estatisticas-full.csv')
df2 = pd.read_csv('campeonato-brasileiro-full.csv', delimiter=",")

#Transformando o dataframe 2 em string
df2 = df2.applymap(str);  

#Criar a coluna Placar para mostrar o placar dos jogos
df2["Placar"] = df2["mandante_Placar"].map(str) + "x" + df2["visitante_Placar"]

#Mostrar dados com a nova coluna
print(f'\nDados com a nova coluna de Placar\n{df2}\n')

#Renomear coluna
df2 = df2.rename(columns={'rodata': 'Rodada'})

#Mostrar dados com a coluna renomeada
print(f'\nCom a coluna renomeada\n{df2}\n')

#Qual time jogou mais como mandante?
contagem_times_mandante = df2['mandante'].value_counts()
print(f'\nOs times jogaram a seguinte quantidade de jogos como mandantes\n{contagem_times_mandante}\n')

#Qual time jogou mais como visitante?
contagem_times_visitante = df2['mandante'].value_counts()
print(f'\nOs times jogaram a seguinte quantidade de jogos como visitantes\n{contagem_times_visitante}\n')

#Nomes dos estados em letra minuscula e uso do apply
def trata_nome(visitante_Estado):
  return visitante_Estado.lower()  
df2['visitante_Estado'] = df2['visitante_Estado'].apply(trata_nome)
print(f'\nNomes dos estados em letra minuscula\n{df2}\n')

#Tratando as duas tabelas com DropNa para tirar valores NaN
print(f'\nMostrando a tabela antes do dropNa\n{df1}\n')

df1 = df1.dropna()
print(f'\nMostrando a tabela após o dropna\n{df1}\n')

df2 = df2.dropna()
print(f'\nMostrar o dropna no segundo dataframe\n{df2}\n')

#Qual a soma dos chutes totais nos jogos da base?
soma_chutes_total = df1['chutes'].sum()
print(f'\nSoma total dos chutes dados nos jogos\n{soma_chutes_total}\n')

#Qual a media de passes nos jogos da base?
media_passes_total = df1['passes'].mean()
print(f'\nA media de passes nos jogos é:\n{media_passes_total}\n')

#Como criar a coluna de media?
df1['Media_Passes'] = df1['passes'].mean()
print(f'\nO DataFrame com a coluna de media\n{df1}\n')

#Qual a mediana de chutes nos jogos da base?
df1['Mediana_Alvo'] = df1['chutes_no_alvo'].median()
print(f'\nO DataFrame com a coluna de mediana\n{df1}\n')

#Quais 3 times com mais faltas?
top_n = 3
times_mais_faltas = df1.nlargest(top_n, 'faltas')['clube']
print(f'\nOs 3 times com mais faltas são:\n{times_mais_faltas}\n')

#Quantas faltas o São Paulo fez?
faltas_sao_paulo = df1.query("clube == 'Sao Paulo'")['faltas']
print(f'O São Paulo fez a seguinte quant de faltas:\n{faltas_sao_paulo}\n')

#Como usar o qcut para mostrar classificações?
quantis = [0, 0.25, 0.50, 0.75, 1]
df1['Classificação_cartoes'] = pd.qcut(df1['cartao_amarelo'], q=quantis, labels=['Muito baixo', 'Baixo', 'Medio', 'Alto'])
print(f'\nA classificação de uso de cartoes amarelos é:\n{df1}\n')

#Exportar um dataframe para um csv
df1.to_csv('dados_times_com_estat.csv', index=True)


#Groupby para numero de vezes que um time aparece na base e quantidade de times em ordem alfabetica
num_times = df1.groupby('clube').size().reset_index(name='Contagem')
print(f'\nA quantidade que um time aparece na base e os times da base são:\n{num_times}\n')

#Grafico de quantidade de faltas por clube
contagem_faltas = df1.groupby('clube')['faltas'].sum()
contagem_faltas.plot(kind='bar', color='red')
plt.title('Quantidade de Faltas por Clube')
plt.xlabel('Clube')
plt.ylabel('Quantidade de Faltas')
plt.show()