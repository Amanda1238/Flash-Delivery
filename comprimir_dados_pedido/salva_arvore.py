class No:
    def __init__(self, caractere=None, frequencia=0, esquerdo=None, direito=None):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerdo = esquerdo
        self.direito = direito

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia


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