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
def obter_livros():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_livro, nome_livro FROM livro")
    dados = cursor.fetchall()
    conn.close()
    return dados

def obter_usuario():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, nome_usuario FROM usuario")
    dados = cursor.fetchall()
    conn.close()
    return dados

def abrir_cadastro_emprestimo(parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar" if id_livro else "Cadastrar emprestimo")
    janela_cad.geometry("550x400")
    
    tk.Label(janela_cad, text="data de devolução", font=("Arial", 10)).pack(pady=10)
    ent_data = tk.Entry(janela_cad, width=30)
    ent_data.pack(pady=5)

    tk.Label(janela_cad, text="data do emprestimo", font=("Arial", 10)).pack(pady=10)
    ent_data2 = tk.Entry(janela_cad, width=30)
    ent_data2.pack(pady=5)

    # Buscamos as categorias do banco
    lista_livros = obter_livros() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]
    lista_usuario = obter_usuario()
    # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_livros = [c[1] for c in lista_livros]
    nome_usuario = [c[1] for c in lista_usuario]

    tk.Label(janela_cad, text="Selecione o livro:").pack(pady=(15, 5))
    
    combo_livro = ttk.Combobox(janela_cad, values=nomes_livros, width=32, state="readonly")
    combo_livro.pack()

    tk.Label(janela_cad, text="Selecione o usuario:").pack(pady=(15, 5))
   
    combo_usuario = ttk.Combobox(janela_cad, values=nome_usuario, width=32, state="readonly")
    combo_usuario.pack()

    def salvar():
        data_devolucao = ent_data.get()
        data_emprestimo = ent_data2.get()
        nome_livro  = combo_livro.get()
        usuario = combo_usuario.get()
        if not data_devolucao.strip():
            messagebox.showwarning("Aviso", "a data de devolução não pode estar vazia.")
            return
        elif not data_emprestimo.strip():
            messagebox.showwarning("Aviso", "a data de emprestimo não pode estar vazia.")
            return
        elif not nome_livro.strip():
            messagebox.showwarning("Aviso", "selecione um livro.")
            return
        elif not usuario.strip():
            messagebox.showwarning("Aviso", "selecione um usuario.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if id_livro:
            # Lógica de Atualização
            cursor.execute("UPDATE livro SET nome_livro = ? WHERE id_livro = ?", (nome_livro, id_livro))
            mensagem = "livro atualizado com sucesso!"
        else:
            # Lógica de Inserção
            cursor.execute("INSERT INTO emprestimo (nome_livro,nome_usuario,data_devolucao,data_emprestimo) VALUES (?,?,?,?)", (nome_livro,usuario,data_devolucao,data_emprestimo))
            mensagem = "livro cadastrado com sucesso!"
            cursor.execute("UPDATE livro SET status = 'emprestado' WHERE nome_livro = ?",(nome_livro,))
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "emprestimo feito com sucesso!")
        janela_cad.destroy()

    btn_texto = "Atualizar" if id_livro else "Salvar"
    btn_cor = "#ffcc00" if id_livro else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

    

    