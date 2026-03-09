import json
from realizar_entrega.realiza_entrega import Motorista

def salvar_motoristas(motoristas, arquivo="motoristas.json"):
    dados = []

    for m in motoristas:
        motorista_dict = {
            "Id_motorista": m.Id_motorista,
            "Lucro_total": m.Lucro_total,
            "Quantidade_de_entregas": m.Quantidade_de_entregas,
            "Quantidade_realizadas": m.Quantidade_realizadas
        }

        dados.append(motorista_dict)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def carregar_motoristas(arquivo="motoristas.json"):

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        motoristas = []

        for m in dados:
            motorista = Motorista(
                Id_motorista=m["Id_motorista"],
                Lucro_total=m["Lucro_total"],
                Quantidade_de_entregas=m["Quantidade_de_entregas"],
                Quantidade_realizadas=m["Quantidade_realizadas"]
            )

            motoristas.append(motorista)

        return motoristas

    except FileNotFoundError:
        return []