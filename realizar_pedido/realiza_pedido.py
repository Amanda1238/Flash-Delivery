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
    desconto_produto: float=0.0

    nome_comprimido: str = None
    tabela_nome: dict = None
    endereco_comprimido: str = None
    tabela_endereco: dict = None



def criar_pedido(listaAdijacensia, enderecos: list[str], nome_cliente: str, id_pedido: int) -> Pedido:
    if len(enderecos) == 0:
        print("\n Não existe bairro cadastrado ")
        print("Cadastre um bairro")
        return None

    origem = random.choice(enderecos)

    if origem not in listaAdijacensia or len(listaAdijacensia[origem]) == 0:
        print(f"\nA origem '{origem}' não possui rotas cadastradas!")
        return None

    destino, tempo = random.choice(listaAdijacensia[origem])

    valor = round(random.uniform(20.0, 200.0), 2)
    peso = random.randint(1, 10)

    return Pedido(
        id_pedido=id_pedido,
        nome_cliente=nome_cliente,
        valor_da_entrega=valor,
        peso_da_mochila=peso,
        endereco=destino,
        tempo_da_entrega=tempo,
        status=0,
        desconto_produto=0.0
    )


def realizar_pedido(listaAdijacensia, endereco: list, historico: list, id_pedido, quantidadePedido):
    if len(endereco) == 0:
        print("\nNão é possível realizar pedidos sem cadastrar bairros!")
        return id_pedido, quantidadePedido

    nome = input("Digite o nome do cliente: ")
    pedido = criar_pedido(listaAdijacensia, endereco, nome, id_pedido)

    if pedido is None:
        return id_pedido, quantidadePedido

    resposta = input("Deseja aplicar desconto no produto? (s/n): ").lower()

    if resposta == 's':
        desconto = float(input("Digite o valor do desconto (%): "))
        pedido.desconto_produto = desconto
        pedido.valor_da_entrega *= (1 - desconto / 100)
        pedido.valor_da_entrega = round(pedido.valor_da_entrega, 2)
        pedido.status = 1
    else:
        pedido.desconto_produto = 0
        pedido.status = 0

    historico.append(pedido)

    print(f"\nPedido criado com sucesso! ID: {id_pedido}")
    print(f"Valor final: R$ {pedido.valor_da_entrega}")
    print(f"Desconto aplicado: {pedido.desconto_produto}%")

    id_pedido += 1
    quantidadePedido += 1
    return id_pedido, quantidadePedido

#0 pedido sem desconto e não entregue
# 1 significa pedido com desconto e não entrege