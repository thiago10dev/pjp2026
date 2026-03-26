preco_unitario=float(input("informe o valor do item:"))
quantidade=float(input("informe a quantidade:"))


def calcular_item(preco_unitario,quantidade):
  
  calculo1=preco_unitario*quantidade
  calculo2=calculo1*0.05
  total_a_pagar=calculo1+calculo2


  return total_a_pagar
print(calcular_item(preco_unitario,quantidade))  
