import time
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