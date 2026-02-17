import json

#--------------------------------------Salva grafo ----------------
def salvar_mapa(endereco, matriz, lista):
    dados = {
        "endereco": endereco,
        "matrizAdijacencia": matriz,
        "listaAdijacensia": lista
    }

    with open("savegrafo.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print("Mapa salvo com sucesso!")
def carregar_mapa():
    try:
        with open("savegrafo.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            print("Mapa carregado com sucesso!")
            return (
                dados["endereco"],
                dados["matrizAdijacencia"],
                dados["listaAdijacensia"]
            )
    except FileNotFoundError:
        print("Nenhum mapa salvo encontrado.")
        return [], [], {}
