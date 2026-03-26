numero=float(input("digite um numero entre 1 e 10:"))
while numero <1 or numero >10:
    numero=float(input("numero invalido digite outro novamente:"))
print(f"numero {numero} é valido")