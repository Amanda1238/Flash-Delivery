from montar_mapa.menu_monta_mapa import listaAdijacensia
def mostrar_lista():
    print("\n=== LISTA DE ADJACÊNCIAS ===")
    for v in listaAdijacensia:
        print(f"{v} -> {listaAdijacensia[v]}")

