def mostrar_matriz(endereco, matrizAdijacencia):
    print("\n=== MATRIZ DE ADJACÊNCIA ===")

    print("     ", end="")
    for nome in endereco:
        print(f"{nome:8}", end="")
    print()

    for i, linha in enumerate(matrizAdijacencia):
        print(f"{endereco[i]:5}", linha)
