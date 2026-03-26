codigo=str(input("digite um codigo de desconto válido: "))
def validar_cupom(CAFÉ10,PROMO5):
   
   if codigo=="CAFÉ10":
    return CAFÉ10
   elif codigo=="PROMO5":
    return PROMO5
   else:
    print("voçê ganhou 0% de desconto")
    return codigo
validar_cupom(0.1,0.05)
