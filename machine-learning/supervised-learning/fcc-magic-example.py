import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Define as colunas dos dados
columns = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans",
        "fAlpha", "fDist", "class"]

# Carrega os dados do arquivo CSV
df = pd.read_csv("../../data/magic04.data", names=columns)

# Mapea os valores de "class" para 0 e 1
df["class"] = df["class"].map({"g": 0, "h": 1})

# Prepara os dados para análise
for label in columns[:-1]:
    plt.hist(df[df["class"] ==0][label], color="blue", label="gamma", alpha=0.7, density=True)
    plt.hist(df[df["class"] == 1][label], color="Red", label="hadron", alpha=0.7, density=True)
    plt.title(label)
    plt.ylabel("probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()

# Separar os dados em Train, Validation e Test
# Split separa os dados; sample em frac retorna porcetagens dos dados
# Cada int representa o tamanho do conjunto de dados
train, valid, test = np.split(df.sample(frac=1), int(0.6 * len(df)),  int(0.8 * len(df)))

# Grandes diferença de escala entre as labels pode causar problemas
# Função para normalizar os dados
def scale_dataset(dataframe):
    x = dataframe[]