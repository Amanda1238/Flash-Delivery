def listar_todos_bairros(enderocos: list):
    if not enderocos:
        print("Não tem endereços cadastrados!")
        return
    print("=============== Listas de Endereços ===============")
    for i in range(len(enderocos)):
        p = enderocos[i]
        print(f"{i+1} : {p} ")
    print("===================================================")


