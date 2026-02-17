from comprimir_dados_pedido.salva_mapa import carregar_mapa
from .adiciona_local import adicionar_local
from .adiciona_rota import adicionar_rota
from .remove_rota import remover_rota
from .mostra_matriz_ADJACENCIA import mostrar_matriz
from .mostrar_lista_ADJACENCIA import mostrar_lista

endereco = []
matrizAdijacencia = []
listaAdijacensia = {}

def montar_menu_mapa():
    global endereco, matrizAdijacencia, listaAdijacensia

    endereco, matrizAdijacencia, listaAdijacensia = carregar_mapa()
    opcao = 20
    while opcao!=0:

        print("\n" + "═" * 45)
        print("             MENU DO MAPA  ")
        print("═" * 45)
        print("   1  -  Adicionar Local")
        print("   2  -  Adicionar Rota")
        print("   3  -  Remover Rota")
        print("   4  -  Mostrar Mapa (Matriz)")
        print("   5  -  Mostrar Mapa (Lista)")
        print("   0  -  Voltar")
        print("═" * 45)

        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue
        match opcao:
            case 1:
                nome = input("Nome do local: ")
                adicionar_local(nome, endereco, listaAdijacensia, matrizAdijacencia)
            case 2:
                if len(endereco) <2:
                    print("Para adicionar rota tem que tem pelo menos dois endereços!")
                    continue
                origem = input("Origem: ")
                if origem not in endereco:
                    print("Origem não existe!")
                    continue

                destino = input("Destino: ")
                if destino not in endereco:
                    print("Destino não existe!")
                    continue
                try:
                    peso = int(input("Distancia em minutos: "))
                except ValueError:
                    print("Distancia inválido!, somente numeros inteiros")
                    continue

                dupla = input("É mão dupla? (s/n): ").lower() == "s"

                adicionar_rota(origem, destino, peso, dupla, endereco, listaAdijacensia, matrizAdijacencia)
            case 3:
                print("Digite a rota que voce quer remover")
                origem = input("Digite o nome da origem do lugar a ser removido: ")
                destino = input("Digite o nome do destino do lugar a ser removido: ")
                remover_rota(origem, destino, endereco, listaAdijacensia, matrizAdijacencia)
            case 4:
                mostrar_matriz(endereco, matrizAdijacencia)
            case 5:
                mostrar_lista(listaAdijacensia)
            case 0:
                print("saindo...")
            case _:
                print("Opção invalida, tente denovo")







