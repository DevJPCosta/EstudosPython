import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados de popularidade de animes e mangás
dados = pd.read_csv(r'C:\Users\joao.santos.SAFIRA\PycharmProjects\pythonProject\dados_popularidade.csv')

# Verificar as primeiras linhas do DataFrame
print(dados.head())

# Analisar os dados e gerar visualizações
ano_popularidade = dados.groupby('Ano')['Popularidade'].mean()

# Gráfico de linha mostrando a média de popularidade ao longo dos anos
plt.plot(ano_popularidade.index, ano_popularidade.values)
plt.xlabel('Ano')
plt.ylabel('Popularidade Média')
plt.title('Popularidade de Animes e Mangás ao longo dos Anos')
plt.show()
