from typing import List
from realizar_pedido.realiza_pedido import realizar_pedido, Pedido
from buscar_pedido.busca_pedido import buscar_pedido
from comprimir_dados_pedido.comprimi_dados import salvar_jogo, carregar_historico
from comprimir_dados_pedido.salva_mapa import salvar_mapa
from comprimir_dados_pedido.salva_motorista import salvar_motoristas, carregar_motoristas
import montar_mapa.menu_monta_mapa as mapa
from montar_mapa.menu_monta_mapa import montar_menu_mapa
from buscar_mapa.busca_mapa import montar_menu_busca_mapa
from realizar_entrega.realiza_entrega import Motorista, realizar_entregas, mostrar_motoristas, finalizar_entregas



# inicio jogo
largura = 70

# quantidade de motorista
motoristas = carregar_motoristas()

if not motoristas:
    motoristas = [
        Motorista(1),
        Motorista(2),
        Motorista(3)
    ]


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
mapa.endereco, mapa.matrizAdijacencia, mapa.listaAdijacensia = mapa.carregar_mapa()


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
           id_pedido, quantidadePedido = realizar_pedido(mapa.listaAdijacensia,mapa.endereco, historico, id_pedido, quantidadePedido)
        case 2:
            buscar_pedido(mapa.endereco, historico, quantidadePedido)
        case 3:
            salvar_jogo(historico, arquivo="savegame.json")
            salvar_mapa(mapa.endereco,mapa.matrizAdijacencia,mapa.listaAdijacensia)
            salvar_motoristas(motoristas)
            print("Jogo salvo com sucesso!\n")
        case 4:
            montar_menu_mapa()
        case 5:
            montar_menu_busca_mapa(mapa.endereco, mapa.listaAdijacensia)
        case 6:
            origem = "centro"
            sucesso = realizar_entregas(motoristas, historico, mapa.listaAdijacensia)
            if sucesso:
                mostrar_motoristas(motoristas, mapa.listaAdijacensia, origem)
                finalizar_entregas(motoristas)
                print("\n Entregas finalizadas com sucesso!\n")
        case 0:
            print("saindo...")
        case _:
            print("Opção invalida, tente denovo")
