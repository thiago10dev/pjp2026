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
def obter_categorias():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_categoria, nome_categoria FROM categoria")
    dados = cursor.fetchall()
    conn.close()
    return dados

def obter_autor():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_autor, nome_autor FROM autor")
    dados = cursor.fetchall()
    conn.close()
    return dados


def abrir_cadastro(parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Cadastrar livro")
    janela_cad.geometry("550x400")
    
    tk.Label(janela_cad, text="Nome do livro:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    # Buscamos as categorias do banco
    lista_categorias = obter_categorias() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]
    lista_autor = obter_autor()
    # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_categorias = [c[1] for c in lista_categorias]
    nome_autor = [ c[1] for c in lista_autor]

    tk.Label(janela_cad, text="Selecione a Categoria:").pack(pady=(15, 5))

    combo_categoria = ttk.Combobox(janela_cad, values=nomes_categorias, width=32, state="readonly")
    combo_categoria.pack()

    tk.Label(janela_cad, text="Selecione o autor:").pack(pady=(15, 5))

    combo_autor = ttk.Combobox(janela_cad,values=nome_autor, width=32, state="readonly")
    combo_autor.pack()
    
    def salvar():
        nome_livro = ent_nome.get()
        categoria = combo_categoria.get()
        autor = combo_autor.get()
        status = "Disponível"
        if not nome_livro.strip():
            messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
            return
        if not categoria.strip():
            messagebox.showwarning("Aviso", "selecione uma categoria.")
            return
        if not autor.strip():
            messagebox.showwarning("Aviso", "selecione um autor.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        
            # Lógica de Inserção
        cursor.execute("INSERT INTO livro (nome_livro,categoria,autor,status) VALUES (?,?,?,?)", (nome_livro,categoria,autor,status,))
        mensagem = "livro cadastrado com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Salvar"
    btn_cor = "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)



 
