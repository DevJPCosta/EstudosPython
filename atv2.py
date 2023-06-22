import matplotlib.pyplot as plt

animes = ['Naruto', 'Attack on Titan', 'One Piece', 'Death Note']
popularidade = [9, 8, 9.5, 8.5]

plt.bar(animes, popularidade)
plt.xlabel('Animes')
plt.ylabel('Popularidade')
plt.title('Popularidade dos Animes')
plt.show()
