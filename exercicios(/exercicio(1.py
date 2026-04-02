"""
Exercicio

1. O Organizador de Compras (Básico)
Objetivo: Criar, adicionar e exibir.
Crie uma lista chamada compras com 3 itens: "Arroz", "Feijão" e "Oleo".
Adicione "Açúcar" ao final da lista usando .append().
Remova o "Feijão" da lista.
Imprima a lista final e mostre quantos itens ela tem no total usando len().

"""
compras=["arroz","feijão","oleo"]
compras.append("açúcar")
compras.remove("feijão")
tamanho = len(compras)
print(compras)
print(tamanho)