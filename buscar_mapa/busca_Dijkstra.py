
def buscar_caminho_rapido(origem, endereco, listaAdjacencia):
    destino = input("Digite o local do destino: ")

    if origem not in endereco or destino not in endereco:
        print("Origem ou destino não existe!")
        return []
    n = len(endereco)
    distancia = [999999] * n
    visitado = [0] * n
    anterior = [""] * n
    indice_origem = endereco.index(origem)
    distancia[indice_origem] = 0

    while True:
        menor_dist = 999999
        atual = -1

        for i in range(n):
            if visitado[i] == 0 and distancia[i] < menor_dist:
                menor_dist = distancia[i]
                atual = i

        if atual == -1:
            break

        visitado[atual] = 1
        nome_atual = endereco[atual]

        for vizinho, peso in listaAdjacencia[nome_atual]:
            indice_viz = endereco.index(vizinho)

            nova_dist = distancia[atual] + peso

            if nova_dist < distancia[indice_viz]:
                distancia[indice_viz] = nova_dist
                anterior[indice_viz] = nome_atual

    caminho = []
    atual = destino

    while atual != "":
        caminho.append(atual)
        if atual == origem:
            break
        indice = endereco.index(atual)
        atual = anterior[indice]

    caminho.reverse()

    if caminho[0] != origem:
        print("Não existe caminho!")
        return []

    print("\n=== Menor caminho encontrado ===")
    print(" → ".join(caminho))
    print(f"Distância total: {distancia[endereco.index(destino)]} min"  )
    print("=================================\n")

