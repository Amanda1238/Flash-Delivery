from typing import List
from realizar_pedido.realiza_pedido import realizar_pedido, Pedido
from buscar_pedido.busca_pedido import buscar_pedido



#@dataclass
#class Motorista:
#    Id_motorista: int
#    Bairro_atual: str
#    Quantidade_mochila: int
#    Lucro_total: float
#    Unidade_de_moedas: int
#    Quantidade_de_entregas: int
#    Pedidos_entregas: List[Pedido] = field(default_factory=list)

# inicio jogo
largura = 70

print("=" * largura)
print("  Seja Bem-Vindo à".center(largura))
print("  Flash Delivery  ".center(largura))
print("-" * largura)
print("Um jogo de logística de entregas!".center(largura))
print("Você será o responsável por comandar toda a operação.".center(largura))
print("=" * largura)
print()
print("Escolha uma das opções do menu principal para começar o jogo!")


# variaveis auxiliares
op = 0
historico: List[Pedido] = []
enderecos = [
    "Alvorada",
    "Boa Vista",
    "Canudos",
    "Centro",
    "Cruzeiro do Sul",
    "Distrito Industrial",
    "Esperança",
    "Jardim América",
    "Jardim das Flores",
    "Jardim Europa",
    "Jardim Panorama",
    "Jardim Primavera",
    "Jardim Vitória",
    "Morada do Sol",
    "Morumbi",
    "Nova Esperança",
    "Parque das Nações",
    "Planalto",
    "Santa Luzia",
    "São Jorge",
    "Vila Rica"
]
id_pedido = 100
quantidadePedido = 0

while op!=6:

    print("╔" + "═" * 55 + "╗")
    print("║{:^55}║".format("  MENU PRINCIPAL  "))
    print("╠" + "═" * 55 + "╣")
    print("║ 1 - Realizar Pedido                                  ║")
    print("║ 2 - Informações do Pedido                            ║")
    print("║ 3 - Salvar o Jogo                                    ║")
    print("║ 4 - Simular o Caminho Mais Curto                     ║")
    print("║ 5 - Realizar Entrega                                 ║")
    print("║ 6 - Sair                                             ║")
    print("╚" + "═" * 55 + "╝")

    try:
        op = int(input("Digite uma opção:"))
    except ValueError:
        print("Digite apenas numeros")
        continue

    match op:
        case 1:
           id_pedido, quantidadePedido = realizar_pedido(enderecos, historico, id_pedido, quantidadePedido)
        case 2:
            buscar_pedido(historico, quantidadePedido)
        case 3:
            print("Salvar jogo")
        case 4:
            print("Simular o caminho mais curto")
        case 5:
            print("realizar entrega")
        case 6:
            print("saindo...")
        case _:
            print("Opção invalida, tente denovo")
