valor_gasto=float(input("informe o valor gasto:"))
def gerar_pontos(valor_gasto):  
    ponto=int(valor_gasto/5)
    return f"voçê ganhou {ponto} pontos pela sua compra"
print(gerar_pontos(valor_gasto))
    
