import pandas as pd
from sklearn_preprocessing import StandardScaler
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split

# Coleta de dados:
df = pd.read_csv("data.csv")

# Limpeza de dados:
df['salario'].fillna(df['salario'].mean(), inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Transformação de dados:
# Normalização:
scaler = StandardScaler() # Transforma valores para média 0 e desvio padrão 1
df['salario_scaled'] = scaler.fit_transform(df[['salario']]) # Lista de args; mesmo passando só 1

df = pd.get_dummies(df, columns=['cidade']) # one-hot enconding

# Detecção e tratamento de outliers:
df = df[(np.abs(stats.zscore(df['salario'])) < 3)] # zscore calcula o quão longe um ponto está na média em desvios padrões
#np.abs() pega valores com zscore maiores que 3; outliers

# Divisão de dados:

x = df.drop('comprou', axis=1) # Features; Retira a coluna 'comprou', que é o target
y = df['comprou'] # Target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # 80% treino, 20% teste