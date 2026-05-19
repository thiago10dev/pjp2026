import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

 

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("./banco_de_dados/banco.db")
    cursor = conn.cursor()
   
    conn.commit()
    return conn
# --- LÓGICA DAS TELAS ---
def cadastrar_autor (parent):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Cadastrar autor")
    janela_cad.geometry("450x300")
    
    tk.Label(janela_cad, text="Nome do autor:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    def salvar():
        nome_autor = ent_nome.get()
        if not nome_autor.strip():
            messagebox.showwarning("Aviso", "O nome não pode estar vazio.")

            return
        
        conn = conectar()
        cursor = conn.cursor()

        # Lógica de Inserção
        cursor.execute("INSERT INTO autor (nome_autor) VALUES (?)", (nome_autor,))
        mensagem = "autor cadastrado com sucesso!"
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Salvar"
    btn_cor =  "lightgreen"
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)