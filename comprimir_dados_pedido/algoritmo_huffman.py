from queue import PriorityQueue
from .salva_arvore import No
# huffman
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