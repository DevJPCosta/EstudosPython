import matplotlib.pyplot as plt

generos = ['Ação', 'Comédia', 'Drama', 'Suspense']
quantidade = [8, 5, 3, 4]

plt.pie(quantidade, labels=generos, autopct='%1.1f%%')
plt.title('Distribuição de Gêneros de Animes')
plt.show()
