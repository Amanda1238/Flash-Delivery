
# monta o grafos dos pedidos

def montar_grafo_pedidos(historico, limite):

    pedidos_validos = [p for p in historico if p.status in (0, 1)]

    grafo = {p.id_pedido: [] for p in pedidos_validos}

    for i in range(len(pedidos_validos)):
        for j in range(i + 1, len(pedidos_validos)):

            p1 = pedidos_validos[i]
            p2 = pedidos_validos[j]

            if p1.endereco != p2.endereco and \
               abs(p1.tempo_da_entrega - p2.tempo_da_entrega) <= limite:

                grafo[p1.id_pedido].append(p2.id_pedido)
                grafo[p2.id_pedido].append(p1.id_pedido)

    return grafo


# tarjan escolhe quais pedidos os motoristas irão entregar

def tarjan_dfs(atual, grafo, ids, low, pilha, na_pilha, componentes, tempo):
    ids[atual] = tempo[0]
    low[atual] = tempo[0]
    tempo[0] += 1

    pilha.append(atual)
    na_pilha.add(atual)

    for viz in grafo[atual]:
        if ids[viz] == -1:
            tarjan_dfs(viz, grafo, ids, low, pilha, na_pilha, componentes, tempo)
            low[atual] = min(low[atual], low[viz])
        elif viz in na_pilha:
            low[atual] = min(low[atual], ids[viz])

    if low[atual] == ids[atual]:
        componente = []
        while True:
            no = pilha.pop()
            na_pilha.remove(no)
            componente.append(no)
            if no == atual:
                break
        componentes.append(componente)


def tarjan_pedidos(grafo):
    tempo = [0]
    ids = {v: -1 for v in grafo}
    low = {v: 0 for v in grafo}
    pilha = []
    na_pilha = set()
    componentes = []

    for v in grafo:
        if ids[v] == -1:
            tarjan_dfs(v, grafo, ids, low, pilha, na_pilha, componentes, tempo)

    return componentes