def filtrar_mangas_por_capitulos(mangas, num_min_capitulos):
    mangas_filtrados = []
    for manga in mangas:
        if manga['capitulos'] > num_min_capitulos:
            mangas_filtrados.append(manga)
    return mangas_filtrados

mangas = [
    {'titulo': 'One Piece', 'capitulos': 1000},
    {'titulo': 'Attack on Titan', 'capitulos': 139},
    {'titulo': 'Berserk', 'capitulos': 364},
    {'titulo': 'Naruto', 'capitulos': 700}
]

mangas_filtrados = filtrar_mangas_por_capitulos(mangas, 200)
print(mangas_filtrados)
