import time
# funçao de busca sequencial
def buscar_nome(historico: list, quantidadePedido: int):
    if quantidadePedido == 0:
        print("Não tem nenhum pedido cadastrado!")
        return

    nomePessoa = input("Digite o nome da Pessoa: ")
    valor_inicial = time.perf_counter()
    print("---------------------------------------------------------------")

    entrou = 0
    encontrou = 0
    encontrados = []

    for p in historico:
        entrou += 1
        if p.nome_cliente.lower() == nomePessoa.lower():
            encontrou = 1
            encontrados.append(p)


    valor_final = time.perf_counter()
    tempo_final = valor_final - valor_inicial

    if encontrou == 1:
        for p in encontrados:
            print("\n+-----------------------------------------------+")
            print(f"| CLIENTE: {p.nome_cliente:<33}|")
            print("+-----------------------------------------------+")
            print(f"| ID..............: {p.id_pedido:<25}|")
            print(f"| VALOR...........: R${p.valor_da_entrega:<23}|")
            print(f"| PESO............: {p.peso_da_mochila:<25}kg|")
            print(f"| ENDEREÇO........: {p.endereco:<25}|")
            print(f"| TEMPO ESTIMADO..: {p.tempo_da_entrega:<22}min|")
            print(f"| STATUS..........: {'Entregue' if p.status == 1 else 'Pendente':<22}|")
            print("+-----------------------------------------------+")
    else:
        print("Nome não foi encontrado!")

    print(f"A busca demorou: {tempo_final:.6f} segundos e entrou {entrou} vezes")
