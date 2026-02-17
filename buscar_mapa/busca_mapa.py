from .busca_DFS import mapear_DFS
from .busca_Dijkstra import buscar_caminho_rapido
from .busca_BFS import mapear_BFS
def montar_menu_busca_mapa(endereco, listaAdjacencia):
    opcao = 20
    while opcao!=0:

        print("\n" + "═" * 45)
        print("             MENU DO MAPA  ")
        print("═" * 45)
        print("   1  -  Explorar mapa DFS")
        print("   2  -  Explorar mapa BFS")
        print("   3  -  Caminho mais rápido")
        print("   0  -  Voltar")
        print("═" * 45)

        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue
        match opcao:
            case 1:
                print("Mapa da busca em Profundidade")
                MapaDfs = mapear_DFS("centro",endereco,listaAdjacencia)
                print(MapaDfs)
            case 2:
                print("Mapa da busca em Largura")
                MapaBfs = mapear_BFS("centro", endereco, listaAdjacencia)
                print(MapaBfs)
            case 3:
                buscar_caminho_rapido("centro", endereco, listaAdjacencia)

            case 0:
                print()
            case _:
                print("Opção invalida, tente denovo")

