# funçao para mostrar todos os pedidos
def listar_todos_historicos(pedidos: list, quantidadePedido: int):
    if quantidadePedido == 0:
        print("Não tem nenhum pedido cadastrado!")
        return
    for i in range(quantidadePedido):
        p = pedidos[i]
        print("\n===================================================")
        print(f"  COMANDA — Pedido nº {i + 1}")
        print("===================================================")
        print(f"  ID..............: {p.id_pedido}")
        print(f"  Cliente.........: {p.nome_cliente}")
        print(f"  Valor...........: R${p.valor_da_entrega}")
        print(f"  Peso............: {p.peso_da_mochila} kg")
        print(f"  Endereço........: {p.endereco}")
        print(f"  Tempo estimado..: {p.tempo_da_entrega} min")
        print(f"  Status..........: {'Entregue' if p.status == 1 else 'Pendente'}")
        print("===================================================")

