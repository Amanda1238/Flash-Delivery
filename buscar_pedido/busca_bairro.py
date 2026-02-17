import time
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