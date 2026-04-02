'''
2. Filtro de Notas (Intermediário - Loops)
Objetivo: Percorrer uma lista e tomar decisões.
Crie uma lista com 10 notas de alunos (ex: [4.5, 7.0, 8.5, 5.0, 10, 6.5, 9.0, 3.0, 7.5, 6.0]).
Use um loop for para criar duas novas listas: aprovados (notas >= 7) e reprovados (notas < 7).
Ao final, exiba as duas listas separadamente.

'''
notas= [4.5, 7.0, 8.5, 5.0, 10, 6.5, 9.0, 3.0, 7.5, 6.0]
for aprovados in notas:
    if aprovados >= 7:
      print(f"aprovados {aprovados}")
for reprovados in notas:
   if reprovados < 7:
      print(f"reprovados {reprovados}")
    