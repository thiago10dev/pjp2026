media=7
nota=0
nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
nota3=float(input("digite a terceira nota:"))
nota4=float(input("digite a quarta nota:"))
nota=(nota1+nota2+nota3+nota4)/4
if nota>media:
    print(f"sua nota final é {nota} voçê está aprovado!")
elif nota==6:
    print(f"sua nota final é {nota} voçê está de recuperção!")
elif nota<6:
    print(f"sua nota final é {nota} voçê está reprovado!")
