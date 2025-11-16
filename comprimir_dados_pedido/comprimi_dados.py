import json
from queue import PriorityQueue
from realizar_pedido.realiza_pedido import Pedido
# huffman

class No:
    def __init__(self, caractere=None, frequencia=0, esquerdo=None, direito=None):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerdo = esquerdo
        self.direito = direito

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def fazer_tabela_Frequencia(Texto: str):
    tabela_frequencia = {}
    for caracter in Texto:
        if caracter in tabela_frequencia:
            tabela_frequencia[caracter] += 1
        else:
            tabela_frequencia[caracter] = 1
    return tabela_frequencia


def gerar_fila_prioridade(Texto: str):
    fila_prioridade = PriorityQueue()

    tabela = fazer_tabela_Frequencia(Texto)
    for caracter,ocorrencia in tabela.items():
        arvore = No(caractere = caracter, frequencia=ocorrencia)
        fila_prioridade.put(arvore)


    return fila_prioridade

def gerar_arvore_dicionario(Texto: str):

    raiz = gerar_fila_prioridade(Texto)

    while raiz.qsize() > 1:
        no1 = raiz.get()
        no2 = raiz.get()

        arvoreSendoGerada = No(caractere=None, frequencia = no1.frequencia + no2.frequencia, esquerdo = no1, direito = no2)

        raiz.put(arvoreSendoGerada)
    return raiz.get()

def percorrer_arvore(no, caminho, tabela_codigos):
    if no is None:
        return

    if no.caractere is not None:
        tabela_codigos[no.caractere] = caminho
        return

    percorrer_arvore(no.esquerdo, caminho + "0", tabela_codigos)

    percorrer_arvore(no.direito, caminho + "1", tabela_codigos)

def gerar_tabela_codigo(Texto: str):
    raiz = gerar_arvore_dicionario(Texto)
    tabela = {}
    percorrer_arvore(raiz, "", tabela)
    return tabela

def codificar_texto(texto: str):
    arvore = gerar_arvore_dicionario(texto)
    tabela = {}
    percorrer_arvore(arvore, "", tabela)

    codigo = ""
    for c in texto:
        codigo += tabela[c]

    return codigo, arvore

def decodificar_texto(codigoFinal: str, arvore: No):
    texto_decodificado = ""
    no_atual = arvore

    for bit in codigoFinal:
        if bit == "0":
            no_atual = no_atual.esquerdo
        else:
            no_atual = no_atual.direito

        if no_atual.caractere is not None:
            texto_decodificado += no_atual.caractere
            no_atual = arvore

    return texto_decodificado
# salva as arvores
def salvar_arvore(no):
    if no is None:
        return None
    return {
        "caractere": no.caractere,
        "frequencia": no.frequencia,
        "esquerdo": salvar_arvore(no.esquerdo),
        "direito": salvar_arvore(no.direito)
    }

def decodificar_arvore(d):
    if d is None:
        return None
    return No(
        caractere=d["caractere"],
        frequencia=d["frequencia"],
        esquerdo=decodificar_arvore(d["esquerdo"]),
        direito=decodificar_arvore(d["direito"])
    )
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
            "status": p.status
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
            d["status"]
        )
        historico.append(p)

    return historico

