# função do troco bottom-up
def troco(valor, notas_moedas):
    valor_centavos = int(round(valor * 100))  # converte para centanvos
    max_val = valor_centavos + 1
    dp = [max_val] * (valor_centavos + 1)
    dp[0] = 0
    escolha = [-1] * (valor_centavos + 1)

    for i, n in enumerate(notas_moedas):
        for v in range(n, valor_centavos + 1):
            if dp[v - n] + 1 < dp[v]:
                dp[v] = dp[v - n] + 1
                escolha[v] = i

    if dp[valor_centavos] == max_val:
        return {}  # quando é impossivel dar troco exato

    resultado = {}
    v = valor_centavos
    while v > 0:
        nota = notas_moedas[escolha[v]]
        resultado[nota] = resultado.get(nota, 0) + 1
        v -= nota

    # converte centavo para reais
    resultado_reais = {f"R$ {n/100:.2f}": q for n, q in resultado.items()}
    return resultado_reais

