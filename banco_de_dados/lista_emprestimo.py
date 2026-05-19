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

def abrir_cadastro(parent, id_emprestimo=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar emprestimo")
    janela_cad.geometry("350x200")
    
    tk.Label(janela_cad, text="Nome usuario:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    # Se for EDIÇÃO, preenche o campo com o nome atual
    if id_emprestimo:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_usuario,data_emprestimo,data_devolucao,nome_livro FROM emprestimo WHERE id_livro = ?", ( id_emprestimo,))
        resultado = cursor.fetchone()
        if resultado:
            ent_nome.insert(0, resultado[0])
        conn.close()
    
    def salvar():
        nome = ent_nome.get()
        if not nome.strip():
            messagebox.showwarning("Aviso", "nenhum campo pode estar vazio.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if id_emprestimo:
            # Lógica de Atualização
            cursor.execute("UPDATE livro SET nome_usuario,data_emprestimo,data_devolucao,nome_livro  = ? WHERE id_emprestimo= ?", (nome, id_emprestimo))
            mensagem = "emprestimo atualizado com sucesso!"
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if id_emprestimo else "Salvar"
    btn_cor = "#ffcc00" if id_emprestimo else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

def abrir_consulta_emprestimo(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar emprestimo")
    janela_con.geometry("880x800") 

    # 1. Tabela (Treeview)
    colunas = ("ID", "Nome do usuario","data do emprestimo","data da devolução","nome de livro")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome do usuario", text="Nome do usuario")
    tabela.heading("data do emprestimo", text="data do emprestimo")
    tabela.heading("data da devolução", text="data da devolução")
    tabela.column("ID", width=50, anchor="center")
    tabela.pack(pady=20, padx=10, fill="both", expand=True)

    # 2. Função interna para o botão Editar
    def executar_edicao():
        item_selecionado = tabela.selection()
        
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione uma opção da lista!")
            return

        valores = tabela.item(item_selecionado, "values")
        id_cat = valores[0]

        # Abre a mesma tela de cadastro, mas agora enviando o ID para modo edição
        abrir_cadastro(parent, id_livro=id_cat)
        janela_con.destroy() 

    # 3. Botões de Ação
    frame_botoes = tk.Frame(janela_con)
    frame_botoes.pack(pady=10)

    btn_editar = tk.Button(
        frame_botoes, 
        text="Editar Selecionada", 
        command=executar_edicao,
        bg="#ffcc00",
        font=("Arial", 10, "bold"),
        width=20
    )
    btn_editar.pack(side="left", padx=5)

    # 4. Buscar dados iniciais
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emprestimo")
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    conn.close()