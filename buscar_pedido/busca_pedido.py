import  time
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

    for p in historico:
        entrou += 1
        if p.nome_cliente == nomePessoa:
            encontrou = 1
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

    valor_final = time.perf_counter()
    tempo_final = valor_final - valor_inicial

    if encontrou == 0:
        print("Nome do cliente não encontrado!")

    print(f"A busca demorou: {tempo_final:.6f} segundos e entrou {entrou} vezes")

# funçao busca binaria
def buscar_bairro(historico: list, quantidadePedido: int):
    if quantidadePedido == 0:
        print("Não tem nenhum pedido cadastrado!")
        return

    buscaBairro = input("digite o nome do bairro para verificar se ele existe: ")

    listaOrdenada = sorted(historico, key=lambda p: p.endereco)
    achouEndereco = 0
    inicio = 0
    fim = len(listaOrdenada) - 1
    entrou = 0
    encontrados = []
    valorInicialTempo = time.perf_counter()

    while inicio <= fim:
        entrou += 1
        meio = (inicio + fim) // 2
        bairroAtual = listaOrdenada[meio].endereco

        if bairroAtual == buscaBairro:
            achouEndereco = 1
            encontrados.append(listaOrdenada[meio])

            #verifica se tem no lado esquerdo
            esquerda = meio - 1
            while esquerda >= 0 and listaOrdenada[esquerda].endereco == buscaBairro:
                entrou += 1
                encontrados.append(listaOrdenada[esquerda])
                esquerda -= 1

            # verifica se tem no lado direito
            direita = meio + 1
            while direita < len(listaOrdenada) and listaOrdenada[direita].endereco == buscaBairro:
                entrou += 1
                encontrados.append(listaOrdenada[direita])
                direita += 1

            inicio = fim + 1

        elif bairroAtual < buscaBairro:
            inicio = meio + 1
        else:
            fim = meio - 1

    valorFinalTempo = time.perf_counter()
    tempoFinal = valorFinalTempo - valorInicialTempo

    if achouEndereco == 1:
        print(f"Ocorrências encontradas do bairro '{buscaBairro}':")
        print("\n=================== PEDIDO ===================")
        for p in encontrados:

            print(f"  ID: {p.id_pedido}")
            print(f"  Cliente: {p.nome_cliente}")
            print(f"  Endereço: {p.endereco}")
            print(f"  Valor: R${p.valor_da_entrega}")
            print(f"  Tempo da entrega: R${p.tempo_da_entrega}")
            print(f"  Status: {'Entregue' if p.status == 1 else 'Pendente'}")
            print("==============================================")

    else:
        print(f"O bairro '{buscaBairro}' não foi encontrado.")

    print(f"A busca demorou: {tempoFinal:.6f} segundos e entrou {entrou} vezes")



def buscar_pedido(historico:list, quantidadePedido: int):
    opcao = 0
    while opcao !=5:
        print("╭" + "─" * 54 + "╮")
        print("│{:^53}│".format(" MENU DE CONSULTAS  "))
        print("├" + "─" * 54 + "┤")
        print("│ 1 - Buscar todos os históricos de pedido             │")
        print("│ 2 - Buscar todas as ocorrências por pessoa           │") #sequencial
        print("│ 3 - Buscar todas as ocorrências por bairro           │") #binario
        print("│ 4 - Buscar todos os pedidos de um certo cliente      │")
        print("│ 5 - Sair                                             │")
        print("╰" + "─" * 54 + "╯")
        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue

        match opcao:
            case 1:
                listar_todos_historicos(historico, quantidadePedido)
            case 2:

                buscar_nome(historico, quantidadePedido)
            case 3:
                buscar_bairro(historico, quantidadePedido)
            case 4:
                print()
            case 5:
                print("Saindo...")
            case _:
                print("Opção invalida!")


