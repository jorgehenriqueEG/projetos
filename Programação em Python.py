import pandas as pd
import seaborn as sns



import matplotlib.pyplot as plt


arquivo = 'seu_arquivo.csv'
dados = pd.read_csv(arquivo)


print("Visualizando as primeiras linhas do dataset:")
print(dados.head())


print("\nInformações gerais sobre o dataset:")
print(dados.info())

print("\nEstatísticas descritivas:")
print(dados.describe())

print("\nVerificando valores nulos:")
print(dados.isnull().sum())

print("\nGerando gráficos...")

coluna = 'coluna'
dados[coluna].hist(bins=20, color='blue', alpha=0.7)
plt.title(f'Histograma da coluna {coluna}')
plt.xlabel(coluna)
plt.ylabel('Frequência')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Correlação')
plt.show()
