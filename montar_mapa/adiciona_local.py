from montar_mapa.menu_monta_mapa import endereco,matrizAdijacencia,listaAdijacensia
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