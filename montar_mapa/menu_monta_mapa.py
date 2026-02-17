from comprimir_dados_pedido.comprimi_dados import carregar_mapa

endereco, matrizAdijacencia, listaAdijacensia = carregar_mapa()
def montar_menu_mapa():
    opcao = 20
    while opcao!=0:

        print("\n" + "═" * 45)
        print("             MENU DO MAPA  ")
        print("═" * 45)
        print("   1  -  Adicionar Local")
        print("   2  -  Adicionar Rota")
        print("   3  -  Remover Rota")
        print("   4  -  Mostrar Mapa (Matriz)")
        print("   5  -  Mostrar Mapa (Lista)")
        print("   0  -  Voltar")
        print("═" * 45)

        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue
        match opcao:
            case 1:
                nome = input("Nome do local: ")
                adicionar_local(nome)
            case 2:
                if len(endereco) <2:
                    print("Para adicionar rota tem que tem pelo menos dois endereços!")
                    continue
                origem = input("Origem: ")
                if origem not in endereco:
                    print("Origem não existe!")
                    continue

                destino = input("Destino: ")
                if destino not in endereco:
                    print("Destino não existe!")
                    continue
                try:
                    peso = int(input("Distancia em minutos: "))
                except ValueError:
                    print("Distancia inválido!, somente numeros inteiros")
                    continue

                dupla = input("É mão dupla? (s/n): ").lower() == "s"

                adicionar_rota(origem, destino, peso, dupla)
            case 3:
                print("Digite a rota que voce quer remover")
                origem = input("Digite o nome da origem do lugar a ser removido: ")
                destino = input("Digite o nome do destino do lugar a ser removido: ")
                remover_rota(origem,destino)
            case 4:
                mostrar_matriz()
            case 5:
                mostrar_lista()
            case 0:
                print("saindo...")
            case _:
                print("Opção invalida, tente denovo")

def adicionar_local(bairro):
    bairros = bairro.lower()
    if bairros in endereco:
        print("Local já existe")
        return

    endereco.append(bairros)
    listaAdijacensia[bairros] = []

    for linha in matrizAdijacencia:
        linha.append(0)
    matrizAdijacencia.append([0]*len(endereco))
    print(f"Local '{bairros}' adicionado.")
def adicionar_rota(origem, destino, peso, dupla):
    if origem == destino:
        print("\nErro: origem e destino não podem ser o mesmo local!")
        return

    i = endereco.index(origem)
    j = endereco.index(destino)

    for destinos, p in listaAdijacensia[origem]:
        if destinos == destino:
            print(f"\nA rota {origem} → {destino} já existe!")
            return
    matrizAdijacencia[i][j] = peso
    listaAdijacensia[origem].append((destino, peso))

    if dupla:
        for origens, p in listaAdijacensia[destino]:
            if origens == origem:
                print(f"\nA rota {destino} → {origem} já existe! (mão dupla)")
                return

        matrizAdijacencia[j][i] = peso
        listaAdijacensia[destino].append((origem, peso))

    print(f"Rota adicionada: {origem} → {destino} ({peso})")
    if dupla:
        print(f"Rota adicionada: {destino} → {origem} ({peso}) Mão dupla")

def remover_rota(origem, destino):
    if origem not in endereco or destino not in endereco:
        print("\nErro: um dos endereços não existe!")
        return
    i = endereco.index(origem)
    j = endereco.index(destino)

    for indice, (d, p) in enumerate(listaAdijacensia[origem]):
        if d == destino:
            listaAdijacensia[origem].pop(indice)
            matrizAdijacencia[i][j] = 0
            print(f"Rota removida: {origem} → {destino}")
            return

    print(f"\nRota {origem} → {destino} não encontrada!")



def mostrar_matriz():
    print("\n=== MATRIZ DE ADJACÊNCIA ===")

    print("     ", end="")
    for nome in endereco:
        print(f"{nome:8}", end="")
    print()

    for i, linha in enumerate(matrizAdijacencia):
        print(f"{endereco[i]:5}", linha)

def mostrar_lista():
    print("\n=== LISTA DE ADJACÊNCIAS ===")
    for v in listaAdijacensia:
        print(f"{v} -> {listaAdijacensia[v]}")

