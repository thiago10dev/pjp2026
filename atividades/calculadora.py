import tkinter as tk
from tkinter import messagebox
import funcao_calculadora as f
valor1=0
valor2=0
resultado=0



def calcular(operacao):
   
    valor1 = float(entry_valor1.get())
    valor2 = float(entry_valor2.get())

    if  operacao == "+" :
        resultado=f.soma (valor1,valor2)
        entry_resultado.insert(0,resultado)
    if  operacao == "-" :
        resultado=f.subtracao (valor1,valor2)
        entry_resultado.insert(0,resultado)
    if  operacao == "*" :
        resultado=f.multiplicacao (valor1,valor2)
        entry_resultado.insert(0,resultado)
    if  operacao == "/" :
        resultado=f.divisao (valor1,valor2)
        entry_resultado.insert(0,resultado)

    

    return resultado
# Criando a janela
root = tk.Tk()
root.title("Calculadora")
root.geometry("1000x500")
 
# Configurando o espaçamento interno da janela
root.config(padx=350, pady=180)
 
# --- ELEMENTOS DA TELA ---
 

 # valor1
tk.Label(root, text="valor1:").grid(row=1, column=0, sticky="W", pady=5)
entry_valor1 = tk.Entry(root, width=30)
entry_valor1.grid(row=1, column=1, pady=5)

# valor2
tk.Label(root, text="valor2:").grid(row=2, column=0, sticky="w", pady=5)
entry_valor2 = tk.Entry(root, width=30)
entry_valor2.grid(row=2, column=1, pady=5)

 #resultado
tk.Label(root, text="resultado:").grid(row=3, column=0, sticky="w", pady=5)
entry_resultado = tk.Entry(root, width=30)
entry_resultado.grid(row=3, column=1, pady=5)


# Botões


btn_soma= tk.Button(root, text="+", command=lambda:(float(calcular("+"))))
btn_soma.grid(row=4, column=0, pady=5, sticky="E")
btn_soma.config(width=10,height=2)

btn_subtracao= tk.Button(root, text="-", command=lambda:(float(calcular("-"))))
btn_subtracao.grid(row=4, column=1,  pady=5, sticky="E" )
btn_subtracao.config(width=10,height=2)

btn_divisao= tk.Button(root, text="/", command=lambda:(float(calcular("/"))))
btn_divisao.grid(row=5, column=0,  pady=5 ,sticky="E")
btn_divisao.config(width=10,height=2)

btn_multiplicacao= tk.Button(root, text="*", command=lambda:(float(calcular("*"))))
btn_multiplicacao.grid(row=5, column=1, pady=5, sticky="E")
btn_multiplicacao.config(width=10,height=2)

root.mainloop()


