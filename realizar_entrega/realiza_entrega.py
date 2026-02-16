CORES = {
    0: "\033[37m",  # aguardando
    1: "\033[34m",  # em rota
    2: "\033[32m",  # prioridade
    3: "\033[31m",  # atrasado
    4: "\033[35m",  # expresso
}
RESET = "\033[0m"

def criar_grafo_pedidos(historico):
    grafo = {}

    for p in historico:
        grafo[p.id_pedido] = []

    for i in range(len(historico)):
        for j in range(i + 1, len(historico)):
            p1 = historico[i]
            p2 = historico[j]

            # conflito: mesmo endereço OU tempo parecido
            if (
                p1.endereco == p2.endereco
                or abs(p1.tempo_da_entrega - p2.tempo_da_entrega) <= 10
            ):
                grafo[p1.id_pedido].append(p2.id_pedido)
                grafo[p2.id_pedido].append(p1.id_pedido)

    return grafo
def welch_powell(grafo):
    # ordena os vértices pelo grau (decrescente)
    vertices = sorted(grafo, key=lambda v: len(grafo[v]), reverse=True)

    cor = {}
    cor_atual = 0

    for v in vertices:
        if v not in cor:
            cor[v] = cor_atual

            for u in vertices:
                if u not in cor:
                    if all(cor.get(viz) != cor_atual for viz in grafo[u]):
                        cor[u] = cor_atual

            cor_atual += 1

    return cor
def colorir_pedidos(historico):
    grafo = criar_grafo_pedidos(historico)
    cores = welch_powell(grafo)

    for p in historico:
        p.status = cores.get(p.id_pedido, 0)
def imprimir_pedidos(historico):
    for p in historico:
        cor = CORES.get(p.status, RESET)
        print(cor + f"Pedido {p.id_pedido} - {p.nome_cliente}")
        print(f"Endereço: {p.endereco}")
        print(f"Valor: R${p.valor_da_entrega}")
        print(f"Desconto: {p.desconto_produto}%")
        print(f"Tempo: {p.tempo_da_entrega} min")
        print("-" * 30 + RESET)
