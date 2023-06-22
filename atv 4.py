class Anime:
    def __init__(self, nome, genero, popularidade, ano_lancamento):
        self.nome = nome
        self.genero = genero
        self.popularidade = popularidade
        self.ano_lancamento = ano_lancamento

    def recomendar_anime_por_genero(self, genero):
        if self.genero == genero:
            return self.nome
        else:
            return None

anime1 = Anime('Naruto', 'Ação', 9, 2002)
anime2 = Anime('Attack on Titan', 'Ação', 8, 2013)
anime3 = Anime('One Piece', 'Aventura', 9.5, 1999)
anime4 = Anime('Death Note', 'Suspense', 8.5, 2006)

recomendacao = anime2.recomendar_anime_por_genero('Ação')
print(recomendacao)
