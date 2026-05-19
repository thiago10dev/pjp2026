import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3



# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("./banco_de_dados/banco.db")
    cursor = conn.cursor()
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS categoria (
    #         id_categoria INTEGER PRIMARY KEY AUTOINCREMENT, 
    #         nome_categoria VARCHAR(100) NOT NULL
    #     )
    # """)
    conn.commit()
    return conn

# --- LÓGICA DAS TELAS ---


def cadastrar_usuarios(parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar" if id_livro else "Cadastrar usuario")
    janela_cad.geometry("1000x500")
    
    tk.Label(janela_cad, text="nome completo", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=100)
    ent_nome.pack(pady=5)

    tk.Label(janela_cad, text="telefone", font=("Arial", 10)).pack(pady=10)
    ent_fone = tk.Entry(janela_cad, width=100)
    ent_fone.pack(pady=5)

    tk.Label(janela_cad, text="endereço", font=("Arial", 10)).pack(pady=10)
    ent_endereco = tk.Entry(janela_cad, width=100)
    ent_endereco.pack(pady=5)

    tk.Label(janela_cad, text="informe o cpf", font=("Arial", 10)).pack(pady=10)
    ent_cpf = tk.Entry(janela_cad, width=100)
    ent_cpf.pack(pady=5)

    tk.Label(janela_cad, text="informe o email", font=("Arial", 10)).pack(pady=10)
    ent_email = tk.Entry(janela_cad, width=100)
    ent_email.pack(pady=5)


    def salvar():
        nome_usuario= ent_nome.get()
        telefone = ent_fone.get()
        endereco = ent_endereco.get()
        cpf = ent_cpf.get()
        email = ent_email.get()
        if not nome_usuario.strip():
            messagebox.showwarning("Aviso", "o nome  não pode estar vazio.")
            return
        elif not telefone.strip():
            messagebox.showwarning("Aviso", "o seu telefone não pode estar vazio.")
            return
        elif not endereco.strip():
            messagebox.showwarning("Aviso", "informe o seu endereço.")
            return
        elif not cpf.strip():
            messagebox.showwarning("Aviso", "informe o seu cpf.")
        elif not email.strip():
            messagebox.showwarning("Aviso", "informe o seu endereço de email.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if id_livro:
            # Lógica de Atualização
            cursor.execute("UPDATE livro SET nome_livro = ? WHERE id_livro = ?", (id_livro))
            mensagem = "livro atualizado com sucesso!"
        else:
            # Lógica de Inserção
            cursor.execute("INSERT INTO usuario (nome_usuario,telefone,endereco,cpf,email) VALUES (?,?,?,?,?)", (nome_usuario,telefone,endereco,cpf,email))
            mensagem = "usuario cadastrado com sucesso!"
            
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "cadastro feito com sucesso!")
        janela_cad.destroy()

    btn_texto = "Atualizar" if id_livro else "Salvar"
    btn_cor = "#ffcc00" if id_livro else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

    

    