
# Distribui os motoristas welsh-powell

def distribuir_motoristas_welsh_powell(motoristas, historico, grafo):
    pedidos_dict = {p.id_pedido: p for p in historico if p.status in (0,1)}

    # ordena os pedidos por ordem decrescente
    vertices = list(grafo.keys())
    vertices.sort(key=lambda v: len(grafo[v]), reverse=True)

    cor_pedidos = {}  # mapa pedido_id é constituido pot cor que representa o motorista

    for v in vertices:
        cores_adj = {cor_pedidos.get(u) for u in grafo[v] if u in cor_pedidos}
        c = 0
        while c in cores_adj:
            c += 1
        cor_pedidos[v] = c

    # atribui motoristas baseados nas cores
    for pedido_id, c in cor_pedidos.items():
        pedido = pedidos_dict[pedido_id]
        motorista = motoristas[c % len(motoristas)]
        motorista.Pedidos_entregas.append(pedido)
        motorista.Quantidade_de_entregas += 1
        motorista.Lucro_total += pedido.valor_da_entrega * 0.10
