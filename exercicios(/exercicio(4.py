"""
4. Sistema de Fila de Banco (Manipulação de Índices)
Objetivo: Entender o conceito de "Primeiro a entrar, primeiro a sair".
Crie uma lista fila = ["Ana", "Carlos", "Beatriz", "Daniel"].
Simule a chegada de um novo cliente ("Eduardo") no fim da fila.
Simule o atendimento do primeiro da fila (remova o índice 0) e guarde o nome dele em uma variável atendido.
Exiba: "O cliente [nome] foi atendido. Restam [lista] na fila."

"""
atendido=[]
fila=["Ana", "Carlos", "Beatriz", "Daniel"]
fila.append("eduardo")
print("estão na fila",fila)
atendido.append(fila[0])
print( fila[0],"foi atendida")
fila.remove(fila[0])
print("estão na fila", fila)