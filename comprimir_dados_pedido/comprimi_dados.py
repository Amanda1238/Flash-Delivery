import json
from realizar_pedido.realiza_pedido import Pedido
from .algoritmo_huffman import codificar_texto, decodificar_texto
from .salva_arvore import salvar_arvore, decodificar_arvore

# funcao do jogo
def salvar_jogo(historico, arquivo="savegame.json"):
    dados = []
    total_original = 0
    total_codificado = 0

    for p in historico:
        nome_cod, nome_arvore = codificar_texto(p.nome_cliente)
        end_cod, end_arvore = codificar_texto(p.endereco)

        tamanho_nome_original = len(p.nome_cliente) * 8
        tamanho_nome_cod = len(nome_cod)
        tamanho_end_original = len(p.endereco) * 8
        tamanho_end_cod = len(end_cod)

        total_original += tamanho_nome_original + tamanho_end_original
        total_codificado += tamanho_nome_cod + tamanho_end_cod

        dados.append({
            "id_pedido": p.id_pedido,
            "nome_cliente": nome_cod,
            "nome_arvore": salvar_arvore(nome_arvore),
            "valor_da_entrega": p.valor_da_entrega,
            "peso_da_mochila": p.peso_da_mochila,
            "endereco": end_cod,
            "end_arvore": salvar_arvore(end_arvore),
            "tempo_da_entrega": p.tempo_da_entrega,
            "status": p.status,
            "desconto_produto": p.desconto_produto
        })

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    reducao = total_original - total_codificado
    percentual = (reducao / total_original * 100) if total_original > 0 else 0
    print(f"\nTamanho total original: {total_original} bits")
    print(f"Tamanho total após compressão: {total_codificado} bits")
    print(f"Redução total: {reducao} bits ({percentual:.2f}%)\n")


def carregar_historico(arquivo="savegame.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        return []

    historico = []

    for d in dados:
        salva_nome = decodificar_arvore(d["nome_arvore"])
        salva_end = decodificar_arvore(d["end_arvore"])

        nome = decodificar_texto(d["nome_cliente"], salva_nome)
        end = decodificar_texto(d["endereco"], salva_end)

        assert nome is not None and len(nome) > 0
        assert end is not None and len(end) > 0

        p = Pedido(
            d["id_pedido"],
            nome,
            d["valor_da_entrega"],
            d["peso_da_mochila"],
            end,
            d["tempo_da_entrega"],
            d["status"],
            d.get("desconto_produto", 0.0) 
        )

        historico.append(p)

    return historico

