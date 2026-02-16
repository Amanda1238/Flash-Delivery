
def montar_menu_busca_mapa(endereco, listaAdjacencia):
    opcao = 20
    while opcao!=0:

        print("\n" + "═" * 45)
        print("             MENU DO MAPA  ")
        print("═" * 45)
        print("   1  -  Explorar mapa DFS")
        print("   2  -  Explorar mapa BFS")
        print("   3  -  Caminho mais rápido")
        print("   0  -  Voltar")
        print("═" * 45)

        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue
        match opcao:
            case 1:
                print("Mapa da busca em Profundidade")
                MapaDfs = mapear_DFS("centro",endereco,listaAdjacencia)
                print(MapaDfs)
            case 2:
                print("Mapa da busca em Largura")
                MapaBfs = mapear_BFS("centro", endereco, listaAdjacencia)
                print(MapaBfs)
            case 3:
                buscar_caminho_rapido("centro", endereco, listaAdjacencia)

            case 0:
                print()
            case _:
                print("Opção invalida, tente denovo")

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

