from dataclasses import dataclass
import random


@dataclass
class Pedido:
    id_pedido: int
    nome_cliente: str
    valor_da_entrega: float
    peso_da_mochila: int
    endereco: str
    tempo_da_entrega: int
    status: int

def criar_pedido(enderecos: list[str], nome_cliente: str, id_pedido: int) -> Pedido:

    tempo_por_bairro = {
        "Alvorada": 5,
        "Boa Vista": 20,
        "Canudos": 120,
        "Centro": 60,
        "Cruzeiro do Sul": 40,
        "Distrito Industrial": 60,
        "Esperança": 30,
        "Jardim América": 120,
        "Jardim das Flores": 120,
        "Jardim Europa": 60,
        "Jardim Panorama": 30,
        "Jardim Primavera": 70,
        "Jardim Vitória": 5,
        "Morada do Sol": 30,
        "Morumbi": 60,
        "Nova Esperança": 120,
        "Parque das Nações": 60,
        "Planalto": 70,
        "Santa Luzia": 150,
        "São Jorge": 30,
        "Vila Rica": 70
    }

    valor = round(random.uniform(20.0, 200.0), 2)
    peso = random.randint(1, 10)
    bairro = random.choice(enderecos)
    entrega = tempo_por_bairro[bairro]

    return Pedido(
        id_pedido=id_pedido,
        nome_cliente=nome_cliente,
        valor_da_entrega=valor,
        peso_da_mochila=peso,
        endereco=bairro,
        tempo_da_entrega=entrega,
        status=0
    )

def realizar_pedido(endereco: list, historico: list,id_pedido, quantidadePedido):

    nome = input("Digite o nome do cliente: ")
    pedido = criar_pedido(endereco, nome, id_pedido)
    historico.append(pedido)
    print(f"\nPedido criado com sucesso! ID: {id_pedido}")

    id_pedido += 1
    quantidadePedido += 1
    return id_pedido, quantidadePedido