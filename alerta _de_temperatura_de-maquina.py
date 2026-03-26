temperatura=float(input("informe a temperatura da caldeira:"))


def verificar_caldeira(temp_atual):
    if temp_atual<90:
        return "aquecimento"
    elif temp_atual<=100:
        return "pronto para usar"
    elif temp_atual>100:
        return "PERIGO:superaquecimento!"
print(verificar_caldeira(temperatura))