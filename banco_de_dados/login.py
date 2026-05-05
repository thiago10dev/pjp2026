import tkinter as tk
from tkinter import messagebox
import sqlite3



def conectar():
    conn = sqlite3.connect("./banco_de_dados/banco.db")
    cursor = conn.cursor()
    cursor.execute("""""")
    conn.commit()
    return conn

def autenticar_dados():
    login = entry_login.get()
    senha = entry_senha.get()
    if login == "adm" and senha =="adm123":
        messagebox.showinfo(":)", "login feito com sucesso!")
        root.destroy()
        import principal
        
        
    elif login!="adm" and senha!="adm123": 
        messagebox.showwarning("Erro", "nome ou senha inválido!")
        
    

# Criando a janela
root = tk.Tk()
root.title("tela de login")
root.geometry("350x200")
 
# Configurando o espaçamento interno da janela
root.config(padx=20, pady=20)
 
# --- ELEMENTOS DA TELA ---
 
# Linha 0: Nome
tk.Label(root, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
entry_login = tk.Entry(root, width=30)
entry_login .grid(row=0, column=1, pady=5)
 
# Linha 1: E-mail
tk.Label(root, text="senha:").grid(row=1, column=0, sticky="w", pady=5)
entry_senha = tk.Entry(root, width=30)
entry_senha.grid(row=1, column=1, pady=5)
 
# Linha 2: Botão (Ocupando duas colunas)
btn_salvar = tk.Button(root, text="entrar", command= autenticar_dados)
btn_salvar.grid(row=2, column=0, columnspan=2, pady=20)
 
root.mainloop()