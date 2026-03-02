# busca o caminho pelo kruskal
def caminho_na_mst(mst, origem, destino, visitados=None):

    if visitados is None:
        visitados = set()

    if origem == destino:
        return [origem]

    visitados.add(origem)

    for vizinho, _ in mst.get(origem, []):
        if vizinho not in visitados:
            caminho = caminho_na_mst(mst, vizinho, destino, visitados)
            if caminho:
                return [origem] + caminho

    return None
