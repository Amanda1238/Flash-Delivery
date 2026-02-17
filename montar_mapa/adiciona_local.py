
def adicionar_local(bairro, endereco, listaAdijacensia, matrizAdijacencia):
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