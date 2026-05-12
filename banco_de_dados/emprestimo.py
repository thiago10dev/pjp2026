import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

#data do emprestimo,data da devolução, id do usuario


# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("./banco_de_dados/banco.db")
    
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

def abrir_cadastro_livro(parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar" if id_livro else "Cadastrar emprestimo")
    janela_cad.geometry("350x200")
    
    # Campo: Seleção de Categoria (Combobox)
    tk.Label(janela_cad, text="Selecione o livro:").pack(pady=(15, 5))
    
    # Buscamos as categorias do banco
    lista_livros = obter_livros() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]
    
    # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_livros = [c[1] for c in lista_livros]
    
    combo_livro = ttk.Combobox(janela_cad, values=nomes_livros, width=32, state="readonly")
    combo_livro.pack()

    # Se for EDIÇÃO, preenche o campo com o nome atual
    def cadastrar_emprestimo():
         conn = conectar()
         cursor = conn.cursor()
         cursor.execute("INSERT INTO emprestimo (id_usuario,id_livro,data_emprestio,data_devolucao) VALUES(?,?,?,?)",())
         dados = cursor.fetchall()
         conn.close()
         return dados
    
    def salvar():
        conn =sqlite3.connect("./banco_de_dados/banco.db")
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso")
        janela_cad.destroy()

    btn_texto = "Atualizar" if id_livro else "Salvar"
    btn_cor = "#ffcc00" if id_livro else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

