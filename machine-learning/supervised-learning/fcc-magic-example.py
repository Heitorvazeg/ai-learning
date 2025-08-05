import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

# Define as colunas dos dados
columns = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans",
        "fAlpha", "fDist", "class"]

# Carrega os dados do arquivo CSV
df = pd.read_csv("../../data/magic04.data", names=columns)

# Mapea os valores de "class" para 0 e 1
df["class"] = df["class"].map({"g": 0, "h": 1})

# Prepara os dados para análise
for label in columns[:-1]:
    plt.hist(df[df["class"] == 0][label], color="blue", label="gamma", alpha=0.7, density=True)
    plt.hist(df[df["class"] == 1][label], color="Red", label="hadron", alpha=0.7, density=True)
    plt.title(label)
    plt.ylabel("probability")
    plt.xlabel(label)
    plt.legend()

# Separar os dados em Train, Validation e Test
# Split separa os dados; sample em frac retorna porcetagens dos dados
# Cada int representa o tamanho do conjunto de dados
train, valid, test = np.split(df.sample(frac=1), [int(0.6 * len(df)),  int(0.8 * len(df))])

# Grandes diferença de escala entre as labels pode causar problemas
# Função para normalizar os dados
# oversample padroniza em quantidade de dados
def scale_dataset(dataframe, oversample=False):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    if oversample:
        ros = RandomOverSampler()
        x, y = ros.fit_resample(x, y)

    data = np.hstack((x, np.reshape(y, (len(y), 1))))

    return data, x, y

# Chama scale_dataset para cada conjunto de dados
train, x_train, y_train = scale_dataset(train, oversample=True)
valid, x_valid, y_valid = (scale_dataset(valid, oversample=False))
test, x_test, y_test = scale_dataset(test, oversample=False)

# Implementação de K-Nearest Neighbors
# metrics fornece metricas para avaliar o modelo
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# Inicia o modelo com 3 vizinhos
knn_model = KNeighborsClassifier(n_neighbors=2)
knn_model.fit(x_train, y_train)

y_pred = knn_model.predict(x_train)

# Implementa classification_report para avaliar o modelo
print(classification_report(y_train, y_pred))