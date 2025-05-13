import pandas as pd
import seaborn as sns

# Análise de Dados em Python

import matplotlib.pyplot as plt

# Carregar os dados (substitua 'seu_arquivo.csv' pelo caminho do seu arquivo de dados)
arquivo = 'seu_arquivo.csv'
dados = pd.read_csv(arquivo)

# Exibir as primeiras linhas do dataset
print("Visualizando as primeiras linhas do dataset:")
print(dados.head())

# Informações gerais sobre o dataset
print("\nInformações gerais sobre o dataset:")
print(dados.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(dados.describe())

# Verificar valores nulos
print("\nVerificando valores nulos:")
print(dados.isnull().sum())

# Visualização de dados
print("\nGerando gráficos...")

# Histograma de uma coluna específica (substitua 'coluna' pelo nome da coluna desejada)
coluna = 'coluna'
dados[coluna].hist(bins=20, color='blue', alpha=0.7)
plt.title(f'Histograma da coluna {coluna}')
plt.xlabel(coluna)
plt.ylabel('Frequência')
plt.show()

# Gráfico de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Correlação')
plt.show()