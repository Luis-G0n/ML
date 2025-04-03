import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar os dados
df = pd.read_csv('diabetes_dataset_with_notes.csv')

# Remover colunas não numéricas para evitar erro na matriz de correlação
df_numeric = df.select_dtypes(include=[np.number])

# Exibir a matriz de correlação
plt.figure(figsize=(12, 6))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
plt.show()

# Selecionar as colunas mais importantes (com maior correlação com 'diabetes')
correlation = df_numeric.corr()['diabetes'].abs().sort_values(ascending=False)
colunas_importantes = correlation[1:6].index.tolist()

# Gerar boxplots das colunas mais importantes
plt.figure(figsize=(12, 6))
df[colunas_importantes].boxplot()
plt.title('Boxplot das Colunas Mais Importantes')
plt.xticks(rotation=45)
plt.show()

# Remover outliers usando o IQR
def remove_outliers(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR
        df = df[(df[col] >= lim_inf) & (df[col] <= lim_sup)]
    return df

df = remove_outliers(df, colunas_importantes)

# Separar variáveis dependentes e independentes
X = df_numeric.drop(columns=['diabetes'], errors='ignore')
y = df_numeric['diabetes']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
acuracia = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {acuracia:.2f}')
