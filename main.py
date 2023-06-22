import csv

# Dados fictícios de popularidade de animes e mangás
dados = [
    {'Ano': 2010, 'Popularidade': 8.5},
    {'Ano': 2011, 'Popularidade': 9.2},
    {'Ano': 2012, 'Popularidade': 7.8},
    {'Ano': 2013, 'Popularidade': 8.9},
    {'Ano': 2014, 'Popularidade': 9.5}
]

# Nome do arquivo CSV
nome_arquivo = 'dados_popularidade.csv'

# Criação do arquivo CSV e escrita dos dados
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    campos = ['Ano', 'Popularidade']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor_csv.writeheader()
    escritor_csv.writerows(dados)

print(f'O arquivo CSV "{nome_arquivo}" foi criado com sucesso!')
