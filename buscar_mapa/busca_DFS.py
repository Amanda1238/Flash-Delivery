def mapear_DFS(inicio, endereco, listaAdjacencia):

    if inicio not in endereco:
        print("Local não encontrado!")
        return []
    n = len(endereco)

    visitado = [0] * n
    caminho = []
    pilha = [inicio]

    while pilha:
        atual = pilha.pop()
        indice = endereco.index(atual)

        if visitado[indice] == 0:
            visitado[indice] = 1
            caminho.append(atual)
            for vizinho, _ in reversed(listaAdjacencia[atual]):
                pilha.append(vizinho)

    return caminho