def remover_rota(origem, destino, endereco, listaAdijacensia, matrizAdijacencia ):
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
