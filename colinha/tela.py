import tkinter as tk
from tkinter import messagebox
import funcao as f
 
def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    if nome and email:
        messagebox.showinfo("Sucesso", f"Cadastro de {nome} realizado!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    mostradados = f.mostra();
    messagebox.showwarning("Erro", f"{mostradados}")

# Criando a janela
root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("350x200")
 
# Configurando o espaçamento interno da janela
root.config(padx=20, pady=20)
 
# --- ELEMENTOS DA TELA ---
 
# Linha 0: Nome
tk.Label(root, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, pady=5)
 
# Linha 1: E-mail
tk.Label(root, text="E-mail:").grid(row=1, column=0, sticky="w", pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, pady=5)
 
# Linha 2: Botão (Ocupando duas colunas)
btn_salvar = tk.Button(root, text="Salvar Cadastro", command=salvar_dados)
btn_salvar.grid(row=2, column=0, columnspan=2, pady=20)
 
root.mainloop()