import time
# busca por um cliente
def buscar_cliente_especifico(historico:list, quantidadePedido:str):
    if quantidadePedido == 0:
        print("Não tem nenhum pedido cadastrado!")
        return

    buscaID = int(input("digite o ID do pedido: "))

    achouEndereco = 0
    inicio = 0
    fim = len(historico) - 1
    entrou = 0

    valorInicialTempo = time.perf_counter()

    while inicio <= fim:
        entrou += 1
        meio = (inicio + fim) // 2
        IdAtual = historico[meio].id_pedido

        if IdAtual == buscaID:
            achouEndereco = 1
            inicio = fim + 1

        elif IdAtual < buscaID:
            inicio = meio + 1
        else:
            fim = meio - 1
    valorFinalTempo = time.perf_counter()
    tempoFinal = valorFinalTempo - valorInicialTempo

    if achouEndereco == 1:
        print(f"ID do cliente '{buscaID}':")
        print("\n=================== PEDIDO ===================")
        print(f"  ID: {historico[meio].id_pedido}")
        print(f"  Cliente: {historico[meio].nome_cliente}")
        print(f"  Endereço: {historico[meio].endereco}")
        print(f"  Valor: R${historico[meio].valor_da_entrega}")
        print(f"  Tempo da entrega: R${historico[meio].tempo_da_entrega}")
        print(f"  Status: {'Entregue' if historico[meio].status == 1 else 'Pendente'}")
        print("==============================================")

    else:
        print(f"O ID '{buscaID}' não foi encontrado.")
    print(f"A busca demorou: {tempoFinal:.6f} segundos e entrou {entrou} vezes")

