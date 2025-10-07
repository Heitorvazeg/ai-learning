# Fundamental para computação científica em python.
# Fornece o array N-dimensional; ndarray; estrutura muito mais eficiente para armazenar e manipular grandes conjuntos de dados.

import numpy as np

# ndarray é uma tabela, vetor ou matriz.
# Homogêneo: Todos os dados devem ser do mesmo tipo.
# Eficiente: Operações otimizadas.

# Pode criar a partir de lista e funções dedicadas também.
arr = np.array([1, 2, 3, 4, 5])
# Número de dimensões do array.
nd = arr.ndim
# Tupla que indica o tamanho de cada dimensão.
sh = arr.shape
# Número total de elementos no array.
s = arr.size
# O tipo de dados do array.
dt = arr.dtype

# Array bidimensional:
arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) # Passa uma lista de argumentos.
# Array tridimensional:
arr_3d = np.array([[[1, 3], [3, 4]], [[5, 6], [7, 8]]])

# funções úteis:
# Cria um array preenchido com zeros.
arr_zeros = np.zeros((3, 4)) # 3 linhas, 4 colunas
arr_ones = np.ones((2, 5)) # Começa com 1
# Cria um array vazio (valores indefinidos)
arr_empt = np.empty(4)

# Slicing:
# Similar às listas python.
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr_2d[0, 1])
print(arr_2d[0, :]) # Pega a linha 0 completa
print(arr_2d[:2, 1:]) # Pega as colunas 1 e 2 nas linhas 0 e 1 

# Pode-se usar expressões booleanas para filtrar dados.
filter = (arr > 2)
print(filter) # Fala se cada indice corresponde à condição
print(arr[filter]) # Pegar os valores que satisfazem

# splits:
spl = np.split(arr, 3) # Divide em 3 arrays
spl_2d = np.hsplit(arr_2d, 3) # Arrays 2d; divide horizontalmente
spl_2d_2 = np.vsplit(arr_2d, 2) # verticalmente

# Operações matemáticas (Vetorializadas):
# Operações aplicadas a vetores. Ótimo para calculos complexos como de ML/DL
soma = arr + 10 # soma = [11, 12, 13, 14, 15], aplica a todos os elementos
mult = arr * 2 # mult = [2, 4, 6, 8, 10]
raiz = np.sqrt(arr) # raiz = [...]

# Entre arrays:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
soma_arrays = a + b # [5, 7, 9]
mult_arrays = a * b # Saída: [ 4 10 18]

# Funções de agregação:
# Soma todos os elementos
total = np.sum(arr)
# Valor minimo
min_v = np.min(arr)
# valor máximo
max_v = np.max(arr)
# média
mean_v = np.mean(arr)
# desvio padrão
desp = np.std(arr)

# Axis operations:
# Pode-se aplicar as funções de agregação em intervalos específicos de arrays multidimensionais.
# axix=0: Operação ao longo das colunas.
# axis=1: Operação ao longo das linhas.
soma_colunas = np.sum(arr_2d, axis=0) # Soma cada coluna e devolve um array
soma_linhas = np.sum(arr_2d, axis=1) # Soma cada linha e devolve um array

# Reshaping:
# Muda a forma do array sem mudar os dados.
matriz_rep = arr.reshape((5, 1)) # Muda para uma matriz com 5 linhas e 1 coluna
matriz_rep2 = arr.reshape((5, -1)) # -1 deixa o numpy decidir o tamanho da dimensão