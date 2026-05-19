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
def obter_emprestimo():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_emprestimo, nome_usuario, data_emprestimo, data_devolucao, nome_livro FROM emprestimo")
    dados = cursor.fetchall()
    conn.close()
    return dados
 
def obter_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, nome_usuario, telefone, cpf, email FROM usuario")
    dados_usu = cursor.fetchall()
    conn.close()
    return dados_usu
def abrir_aplicar_multa (parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title( "aplicar multa")
    janela_cad.geometry("450x300")

    tk.Label(janela_cad, text="valor da multa:", font=("Arial", 10)).pack(pady=10)
    ent_valor = tk.Entry(janela_cad, width=30)
    ent_valor.pack(pady=5)
    # Buscamos as categorias do banco
    lista_emprestimo = obter_emprestimo() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]
    lista_usuarios = obter_usuarios()
 
    # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_emprestimo = [c[0] for c in lista_emprestimo]
    nomes_usuarios = [c[1] for c in lista_usuarios]

    tk.Label(janela_cad, text="Selecione o id do emprestimo:").pack(pady=(15, 5))
    combo_emprestimo = ttk.Combobox(janela_cad, values=nomes_emprestimo, width=32, state="readonly")
    combo_emprestimo.pack()
 
    tk.Label(janela_cad, text="selecione o usuario:").pack(pady=(15, 5))
    combo_usuario = ttk.Combobox(janela_cad, values=nomes_usuarios, width=32, state="readonly")
    combo_usuario.pack()

    def salvar():
        valor_multa = ent_valor.get()
        emprestimo  = combo_emprestimo.get()
        usuario = combo_usuario.get()
 
        if not valor_multa.strip():
            messagebox.showwarning("Aviso", "informe o valor da multa.")
            return
        conn = conectar()
        cursor = conn.cursor()
        if id_livro:
            # Lógica de Atualização
            cursor.execute("UPDATE livro SET nome_livro = ? WHERE id_livro = ?", ())
            mensagem = "livro atualizado com sucesso!"
        else:
            # Lógica de Inserção
            cursor.execute("INSERT INTO multa (nome_usuario,id_emprestimo,valor_multa) VALUES (?,?,?)", (usuario,emprestimo,valor_multa))
            mensagem = "multa aplicada com sucesso!"
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Salvar"
    btn_cor = "lightgreen"
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)