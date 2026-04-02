"""
5. Buscador de Nomes (Busca em Listas)
Objetivo: Verificar a existência de itens.

Crie uma lista com nomes de convidados para uma festa.
Peça ao usuário para digitar um nome.
O programa deve verificar se o nome está na lista (usando o operador in ou um loop):
Se estiver: Exiba "Bem-vindo! Nome na lista."
Se não estiver: Exiba "Desculpe, seu nome não consta aqui."

"""
nomes_convidados=["ana","maria","davi","joão"]

nome_informado=str(input("informe o seu nome:"))
if nome_informado in nomes_convidados:
     print(f"seja bem-vindo a festa {nome_informado}")
else:
    print("desculpe, seu nome não está na lista!")