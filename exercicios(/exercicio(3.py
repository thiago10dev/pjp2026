"""
3. O Analista de Números (Lógica e Funções de Lista)
Objetivo: Usar funções prontas do Python para análise.
Peça para o usuário digitar 5 números inteiros e guarde-os em uma lista.
Depois de preenchida, o programa deve informar:
O maior número digitado (max).
O menor número digitado (min).
A soma de todos os números (sum).
A média aritmética dos números.

"""
lista_numeros=[]
contador=0
while contador < 5:
    contador+=1
    print("digite abaixo numeros inteiros ")
    numeros=int(input(":"))
    lista_numeros.append(numeros)

print(f"numeros digitados {lista_numeros}")
print("o maior número digitado foi",max(lista_numeros))
print("o menor número digitado foi",min(lista_numeros))

