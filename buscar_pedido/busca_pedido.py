from .busca_todos_historicos import listar_todos_historicos
from .busca_nome import buscar_nome
from .busca_bairro import buscar_bairro
from .busca_cliente_especifico import buscar_cliente_especifico
from .buscar_associacao_por_nome import buscar_associacao_nome
from .busca_todos_bairros_cadastrados import listar_todos_bairros



def buscar_pedido(endereco,historico:list, quantidadePedido: int):
    opcao = 20
    while opcao != 0:
        print("╭" + "─" * 54 + "╮")
        print("│{:^53}│".format(" MENU DE CONSULTAS  "))
        print("├" + "─" * 54 + "┤")
        print("│ 1 - Buscar todos os históricos de pedido             │")# sequencial
        print("│ 2 - Buscar todas as ocorrências por pessoa           │")# sequencial
        print("│ 3 - Buscar todas as ocorrências por bairro           │")# binario
        print("│ 4 - Buscar pelo um cliente especifico                │")# binario
        print("│ 5 - Buscar uma associação do nome do cliente         │")# Rabin-Karp
        print("│ 6 - Buscar todos os enderecos cadastrados            │")#sequencial
        print("│ 0 - Sair                                             │")
        print("╰" + "─" * 54 + "╯")
        try:
            opcao = int(input("Digite uma opção:"))
        except ValueError:
            print("Digite apenas numeros")
            continue

        match opcao:
            case 1:
                listar_todos_historicos(historico, quantidadePedido)
            case 2:
                buscar_nome(historico, quantidadePedido)
            case 3:
                buscar_bairro(historico, quantidadePedido)
            case 4:
                buscar_cliente_especifico(historico, quantidadePedido)
            case 5:
                buscar_associacao_nome(historico, quantidadePedido)
            case 6:
                listar_todos_bairros(endereco)
            case 0:
                print("Saindo...")
            case _:
                print("Opção invalida!")


