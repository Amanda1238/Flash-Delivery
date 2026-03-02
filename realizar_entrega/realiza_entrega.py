from dataclasses import dataclass, field
from typing import List
from realizar_pedido.realiza_pedido import Pedido
from .Kruskal_mapa_delivery import kruskal_cidade
from .caminho_na_mst import caminho_na_mst
from .problema_troco import troco
from .montar_pedido_tarjan import montar_grafo_pedidos, tarjan_pedidos
from .distribui_motorista_welshPower import distribuir_motoristas_welsh_powell

# Classe Motorista
@dataclass
class Motorista:
    Id_motorista: int
    Lucro_total: float = 0
    Quantidade_de_entregas: int = 0
    Quantidade_realizadas: int = 0
    Pedidos_entregas: List[Pedido] = field(default_factory=list)
    historico_entregas: List[Pedido] = field(default_factory=list)

# finaliza as entregas
def finalizar_entregas(motoristas):
    for m in motoristas:
        # Soma no total acumulado
        m.Quantidade_realizadas += m.Quantidade_de_entregas

        # atualiza o historico
        for p in m.Pedidos_entregas:
            p.status = 2  # entregue
            m.historico_entregas.append(p) # adiciona no historico do motorista

        # Limpa apenas o ciclo atual
        m.Pedidos_entregas.clear()
        m.Quantidade_de_entregas = 0
        m.Lucro_total = 0

# realiza as entregas
def realizar_entregas(motoristas, historico, listaAdj):
    pendentes = [p for p in historico if p.status in (0, 1)]
    if not pendentes:
        print("\nNão há pedidos pendentes.")
        return False

    limite = 10

    # limpa a classe motorista antes de realizar entrega
    for m in motoristas:
        m.Pedidos_entregas.clear()
        m.Quantidade_de_entregas = 0
        m.Lucro_total = 0

    # monta os grafos dos pedidos
    grafo_pedidos = montar_grafo_pedidos(historico, limite)

    # usa tarjan para identificar os componentes
    componentes = tarjan_pedidos(grafo_pedidos)

    # aplica a coloração para cada componente
    for comp in componentes:
        subgrafo = {v: [u for u in grafo_pedidos[v] if u in comp] for v in comp}
        distribuir_motoristas_welsh_powell(motoristas, historico, subgrafo)

    print("\nEntregas distribuídas com sucesso :)!\n")
    return True


def mostrar_motoristas(motoristas, listaAdj, origem="centro"):
    # gera o mapa da cidade
    mst = kruskal_cidade(listaAdj)

    # Notas e moedas disponíveis (em centavos)
    notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

    print("\n RELATÓRIO COMPLETO DOS MOTORISTAS (KRUSKAL)\n")

    for m in motoristas:
        print("=" * 60)
        print(f" Motorista ID: {m.Id_motorista}")
        print(f" Entregas no Ciclo Atual: {m.Quantidade_de_entregas}")
        print(f" Total de Entregas Realizadas: {m.Quantidade_realizadas}")
        print(f" Lucro do Ciclo Atual: R$ {m.Lucro_total:.2f}")
        print("-" * 60)

        if not m.Pedidos_entregas:
            print(" Nenhuma entrega atribuída neste ciclo.")
        else:
            ponto_atual = origem
            rota_total = []

            for pedido in m.Pedidos_entregas:
                print(f"\n Pedido ID: {pedido.id_pedido}")
                print(f"   Endereço: {pedido.endereco}")
                print(f"   Valor Entrega: R$ {pedido.valor_da_entrega:.2f}")
                print(f"   Tempo estimado: {pedido.tempo_da_entrega} min")

                if pedido.status == 2:
                    status_txt = "Entregue"
                elif pedido.status == 1:
                    status_txt = "Pendente (com desconto)"
                else:
                    status_txt = "Pendente"

                print(f"   Status: {status_txt}")

                # usa programação dinamica, algoritmo do troco
                troco_entrega = troco(pedido.valor_da_entrega, notas_moedas)
                if troco_entrega:
                    print("   Notas/Moedas recebidas:")
                    for nota, qtd in sorted(
                        troco_entrega.items(),
                        key=lambda x: -float(x[0].replace("R$ ", ""))
                    ):
                        print(f"      {qtd} x {nota}")
                else:
                    print("   Troco exato não possível.")

                # percore a rota
                caminho = caminho_na_mst(mst, ponto_atual, pedido.endereco)
                if caminho:
                    print(f"   Rota: {' → '.join(caminho)}")
                    if not rota_total:
                        rota_total.extend(caminho)
                    else:
                        rota_total.extend(caminho[1:])
                    ponto_atual = pedido.endereco
                else:
                    print("   Caminho não encontrado. :(")
                print()
                print("------------------------------------------------------------------------------")

            print("\nROTA COMPLETA PERCORRIDA:")
            print("   " + " → ".join(rota_total))

        # mostra o historico do motorista
        if m.historico_entregas:
            print("\nHISTÓRICO DE ENTREGAS DO MOTORISTA:")
            for p in m.historico_entregas:
                status_txt = "Entregue" if p.status == 2 else "Pendente"
                print(f"  - Pedido {p.id_pedido} | {p.endereco} | Status: {status_txt}")

        print("=" * 60)
        print()