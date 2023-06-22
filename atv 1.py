def buscar_animes_por_genero(animes, genero):
    animes_por_genero = []
    for anime in animes:
        if anime['genero'] == genero:
            animes_por_genero.append(anime)
    return animes_por_genero

animes = [
    {'nome': 'Naruto', 'genero': 'Ação', 'episodios': 500},
    {'nome': 'Attack on Titan', 'genero': 'Ação', 'episodios': 75},
    {'nome': 'One Piece', 'genero': 'Aventura', 'episodios': 1000},
    {'nome': 'Death Note', 'genero': 'Suspense', 'episodios': 37}
]

animes_acao = buscar_animes_por_genero(animes, 'Ação')
print(animes_acao)
