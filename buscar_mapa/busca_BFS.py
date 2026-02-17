def mapear_BFS(oriegem, endereco, listaAdjacencia):
    if oriegem not in endereco:
        print("Local não encontrado!")
        return []
    n = len(endereco)
    visitados = [0] * n
    caminho = []
    fila = [oriegem]
    while fila:
        atual = fila.pop(0)
        indice = endereco.index(atual)
        if visitados[indice] == 0:
            visitados[indice] = 1
            caminho.append(atual)
            for vizinho, _ in listaAdjacencia[atual]:
                fila.append(vizinho)
    return caminho