# Biblioteca para visualização de dados.

import matplotlib.pyplot as plt

# Figure: É a janela inteira onde o gráfico é desenhado.
# Axes: É o gráfico individual (Linhas, barras...) que plotamos.

# Fornece dados para os eixos x e y.
meses = ["Jan", "Fev", "Mar", "Abr"]
vendas = [100, 150, 90, 200]

fig, ax = plt.subplots() # figure e eixos
ax.plot(meses, vendas)

ax.set_title("Vendas por mês") # Título do gráfico
ax.set_xlabel("Meses") # Rótulo para o eixo x
ax.set_ylabel("Vendas") # Rótulo para o eixo y

plt.show() # Mostra o gráfico

# Gráfico de Barras:
# Plota valores de diferentes categorias.
categorias = ['Produto A', 'Produto B', 'Produto C']
valores = [450, 720, 300]

ax.bar(categorias, valores, color='skyblue')
ax.set_title("Comparativo de Vendas por Produto")
ax.set_ylabel("Total de vendas")

plt.show()

# Multigráficos:
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4)) # Matriz de Eixos (1 linha, 2 colunas)