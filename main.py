from dataclasses import dataclass, field
from typing import List
from realizar_pedido.realiza_pedido import realizar_pedido, Pedido
from buscar_pedido.busca_pedido import buscar_pedido
from comprimir_dados_pedido.comprimi_dados import salvar_jogo, carregar_historico, salvar_mapa
from montar_mapa.monta_mapa import endereco,matrizAdijacencia,listaAdijacensia, montar_menu_mapa
from buscar_mapa.busca_mapa import montar_menu_busca_mapa
from realizar_entrega.realiza_entrega import colorir_pedidos, imprimir_pedidos

@dataclass
class Motorista:
    Id_motorista: int
    Lucro_total: float
    Quantidade_de_entregas: int
    Pedidos_entregas: List[Pedido] = field(default_factory=list)

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
op = 20
historico: List[Pedido] = carregar_historico(arquivo="savegame.json")
quantidadePedido = len(historico)

id_pedido = 100 + quantidadePedido

while op!=0:

    print("╔" + "═" * 55 + "╗")
    print("║{:^55}║".format("  MENU PRINCIPAL  "))
    print("╠" + "═" * 55 + "╣")
    print("║ 1 - Realizar Pedido                                  ║")
    print("║ 2 - Informações do Pedido                            ║")
    print("║ 3 - Salvar o Jogo                                    ║")
    print("║ 4 - Montar o mapa do jogo                            ║")
    print("║ 5 - Buscas pelo mapa                                 ║")
    print("║ 6 - Realizar Entrega                                 ║")
    print("║ 0 - Sair                                             ║")
    print("╚" + "═" * 55 + "╝")

    try:
        op = int(input("Digite uma opção:"))
    except ValueError:
        print("Digite apenas numeros")
        continue

    match op:
        case 1:
           id_pedido, quantidadePedido = realizar_pedido(listaAdijacensia,endereco, historico, id_pedido, quantidadePedido)
        case 2:
            buscar_pedido(endereco, historico, quantidadePedido)
        case 3:
            salvar_jogo(historico, arquivo="savegame.json")
            salvar_mapa(endereco,matrizAdijacencia,listaAdijacensia)
            print("Jogo salvo com sucesso!\n")
        case 4:
            montar_menu_mapa()
        case 5:
            montar_menu_busca_mapa(endereco,listaAdijacensia)
        case 6:
            print("construindo")
        case 0:
            print("saindo...")
        case _:
            print("Opção invalida, tente denovo")
