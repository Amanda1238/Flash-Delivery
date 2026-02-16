import time
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

        if bairroAtual.lower() == buscaBairro.lower():
            achouEndereco = 1
            encontrados.append(listaOrdenada[meio])

            #verifica se tem no lado esquerdo
            esquerda = meio - 1
            while esquerda >= 0 and listaOrdenada[esquerda].endereco.lower() == buscaBairro.lower():
                entrou += 1
                encontrados.append(listaOrdenada[esquerda])
                esquerda -= 1

            # verifica se tem no lado direito
            direita = meio + 1
            while direita < len(listaOrdenada) and listaOrdenada[direita].endereco.lower() == buscaBairro.lower():
                entrou += 1
                encontrados.append(listaOrdenada[direita])
                direita += 1

            inicio = fim + 1

        elif bairroAtual.lower() < buscaBairro.lower():
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


# busca de texto
def auxiliar_rabin_karp(texto: str, palavraProcurada: str):

    if not palavraProcurada:
        return False

    texto = texto.lower()
    palavraProcurada = palavraProcurada.lower()
    tamanhoTexto = len(texto)
    tamanhoPalavraProcurada = len(palavraProcurada)

    if tamanhoTexto < tamanhoPalavraProcurada:
        return False

    base = 256
    mod = 101

    high_base = 1
    for _ in range(tamanhoPalavraProcurada - 1):
        high_base = (high_base * base) % mod

    hash_p = 0
    hash_t = 0
    for i in range(tamanhoPalavraProcurada):
        hash_p = (hash_p * base + ord(palavraProcurada[i])) % mod
        hash_t = (hash_t * base + ord(texto[i])) % mod

    for i in range(tamanhoTexto - tamanhoPalavraProcurada + 1):

        if hash_t == hash_p and texto[i:i+tamanhoPalavraProcurada] == palavraProcurada:
            return True

        if i < tamanhoTexto - tamanhoPalavraProcurada:
            hash_t = (hash_t - ord(texto[i]) * high_base) % mod
            hash_t = (hash_t * base + ord(texto[i + tamanhoPalavraProcurada])) % mod
            hash_t %= mod

    return False

def buscar_associacao_nome(historico: list, quantidadePedido: int):

    if quantidadePedido == 0:
        print("Não tem nenhum pedido cadastrado!")
        return

    encontrados = []
    padrao = input("Digite o padrao que você quer encontrar: ")

    tempo_inicial = time.perf_counter()

    for pedido in historico:
        padraoEncontrado = auxiliar_rabin_karp(pedido.nome_cliente, padrao)
        if padraoEncontrado == True:
            encontrados.append(pedido)

    tempo_final = time.perf_counter()
    tempo_final = tempo_final - tempo_inicial

    if encontrados:
        print(f"\nPedidos encontrados para '{padrao}':\n")
        print(f"{'ID':<4} | {'Cliente':<20} | {'Valor':<10} | {'Peso':<5} | "
              f"{'Endereço':<20} | {'Tempo(min)':<10} | {'Status':<6}")
        print("-" * 95)

        for pedido in encontrados:
            print(f"{pedido.id_pedido:<4} | "
                  f"{pedido.nome_cliente:<20} | "
                  f"R${pedido.valor_da_entrega:<9.2f} | "
                  f"{pedido.peso_da_mochila:<5} | "
                  f"{pedido.endereco:<20} | "
                  f"{pedido.tempo_da_entrega:<10} | "
                  f"{pedido.status:<6}")
    else:
        print(f"Nenhum pedido encontrado com  padrão '{padrao}'.")
    print(f"A busca demorou: {tempo_final:.6f} segundos ")

def listar_todos_bairros(enderocos: list):
    if not enderocos:
        print("Não tem endereços cadastrados!")
        return
    print("=============== Listas de Endereços ===============")
    for i in range(len(enderocos)):
        p = enderocos[i]
        print(f"{i+1} : {p} ")
    print("===================================================")



def buscar_pedido(endereco,historico:list, quantidadePedido: int):
    opcao = 20
    while opcao != 0:
        print("╭" + "─" * 54 + "╮")
        print("│{:^53}│".format(" MENU DE CONSULTAS  "))
        print("├" + "─" * 54 + "┤")
        print("│ 1 - Buscar todos os históricos de pedido             │")# sequencial
        print("│ 2 - Buscar todas as ocorrências por pessoa           │")# sequencial
        print("│ 3 - Buscar todas as ocorrências por bairro           │")# binario
        print("│ 4 - Buscar pelo um cliente especifico                │")# binario
        print("│ 5 - Buscar uma associação do nome do cliente         │")# Rabin-Karp
        print("│ 6 - Buscar todos os enderecos cadastrados            │")#sequencial
        print("│ 0 - Sair                                             │")
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
                buscar_cliente_especifico(historico, quantidadePedido)
            case 5:
                buscar_associacao_nome(historico, quantidadePedido)
            case 6:
                listar_todos_bairros(endereco)
            case 0:
                print("Saindo...")
            case _:
                print("Opção invalida!")


