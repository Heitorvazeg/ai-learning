# Biblioteca mais utilizada para análise e manipulação de dados.

import pandas as pd

# Series: Estrutura unidimensional, similar a um array.
# DatFrame: Estrutura bidimensional, similar a uma tabela.

# Cria um dataframe a partir de um dicionário.
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [28, 34, 29]
}
df = pd.DataFrame(dados)
print(df) # Printa em formato de tabela

# Visualizando:
n = 5
df.head(n) # Mostra as primeiras n linhas
df.tail(n) # Mostra as últimas n linhas
print(df.info()) # Tipo de dados de cada colunas, não nulos, memória...
df.shape # Tupla com número de linhas e colunas
print(df.describe()) # Estatísticas descritivas: média, desvio padrão, minimo...

# Leitura e escrita de Arquivos:
colunas = ["A", "B", "C"]
pd.read_csv('arquivo.csv', name=colunas) # Lê CSV e aplica os nomes para as colunas
# pd.read_csv('arquivo.csv') # lê CSV
# pd.to_csv('arquivo.csv') # Escreve em um arquivo CSV

# pd.read_excel('arquivo.xlsx') # Excel
# pd.to_excel('arquivo.xlsx') # Escreve

# Seleção e filtragem:
# Por colunas:
idades = df['Idade'] # Retorna uma Series. Seleciona uma coluna específica
subset = df[['Nome', 'Idade']] # Retorna um dataframe. Múltiplas colunas; Tem um array de args, as colunas.
# Por filtros:
condicao = df['Idade'] > 20 # Aplica condição booleana em cada elemento
df_cond = df[condicao] # Dataframe que satisfaz a condição
# Indexação:
# .loc[] é por rótulo (label)
dado_bruno = df.loc[1, ['Nome', 'Idade']] # Seleciona a linha 1 das colunas Nome e Idade
# .iloc[] é por posição; precisa saber exatamente a posição do que deseja
idade_ana = df.iloc[0, 1] # seleciona o elemento na linha 0, coluna 1

# Manipulação e Limpeza de dados:
df['Nova'] = df['Vendas'] * 0.10 # cria uma nova coluna
df['Idade'] = df['Idade'] + 1 # Modifica uma coluna existente

# Tratamento de Valores:
df_limpo = df.dropna() # Remove linhas com valores nulos

# Substitui nulos pela média
media = df['Vendas'].mean()
df['Vendas'] = df['Vendas'].fillna(media)