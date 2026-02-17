
def adicionar_rota(origem, destino, peso, dupla, endereco, listaAdijacensia, matrizAdijacencia):
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
