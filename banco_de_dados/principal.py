import tkinter as tk
from tkinter import ttk, messagebox
import categoria_padrao
import livro
import sqlite3
import datetime
import emprestimo
import cadastro_usuarios

def realizar_backup(db_origem, db_destino):
    try:
        # Conecta ao banco de dados principal (origem)
        conn_origem = sqlite3.connect(db_origem)
        # Conecta (ou cria) o arquivo de backup (destino)
        conn_destino = sqlite3.connect(db_destino)
 
        # Executa o backup
        with conn_destino:
             conn_origem.backup(conn_destino)
        print(f"Backup concluído com sucesso em: {db_destino}")
        messagebox.showinfo(":)", "backup feito com sucesso!")
 
    except sqlite3.Error as e:
        print(f"Erro ao realizar backup: {e}")

    finally:
        conn_origem.close()
        conn_destino.close()
 
data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_backup = f"./banco_de_dados/backup_sistema_{data_atual}.db"
# Use este nome no destino do backup

# Exemplo de uso


# --- MENU PRINCIPAL (ROOT) ---
root = tk.Tk()
root.title("Menu Principal - Sistema de Biblioteca")
root.geometry("400x500")

# 1. Criar a barra de menu principal
barra_menu = tk.Menu(root)

# 2. Criar o menus
menu_categorias = tk.Menu(barra_menu, tearoff=0)
menu_backup = tk.Menu(barra_menu, tearoff=1)

# Adicionando as opções dentro do menu Categorias 

#botão categoria
menu_categorias.add_command(label="Cadastrar Nova", command=lambda: categoria_padrao.abrir_form_categoria(root))
menu_categorias.add_command(label="Consultar Todas", command=lambda: categoria_padrao.abrir_consulta(root))
menu_categorias.add_separator() # Linha divisória

#botão de backup
menu_backup.add_command(label="realizar backup", command=lambda: realizar_backup('./banco_de_dados/banco.db',nome_backup))



#  Adiciona o menu à barra principal

barra_menu.add_cascade(label="Categorias", menu=menu_categorias)
barra_menu.add_cascade(label="backup", menu=menu_backup)

# 5. Configurar a janela para usar esta barra de menu
root.config(menu=barra_menu)

tk.Label(root, text="GERENCIADOR BIBLIOTECA", font=("Arial", 14, "bold")).pack(pady=30)

btn_cadastrar = tk.Button(root, text="NOVO CADASTRO  DE CATEGORIA", width=30, height=2, 
                          command=lambda:categoria_padrao.abrir_cadastro(root), bg="#e1e1e1")
btn_cadastrar.pack(pady=10)

# O lambda cria um "adiamento". A função só roda no clique.
btn_consultar = tk.Button(
    root, 
    text="CONSULTAR LISTA DE CATEGORIA", width=30,height=2,
    command=lambda: categoria_padrao.abrir_consulta(root), 
    bg="#e1e1e1"
)
btn_consultar.pack(pady=10)

btn_cadastrar_livro = tk.Button(root, text="NOVO CADASTRO DE LIVRO", width=30, height=2, 
                          command=lambda:livro.abrir_cadastro(root), bg="#e1e1e1")
btn_cadastrar_livro.pack(pady=10)

btn_cadastrar_emprestimo = tk.Button(root, text="NOVO CADASTRO DE EMPRÉSTIMO", width=30 , height=2,
                                  command=lambda:emprestimo.abrir_cadastro_emprestimo(root), bg ="#e1e1e1")
btn_cadastrar_emprestimo.pack(pady=10)

btn_cadastrar_usuario = tk.Button(root, text="NOVO CADASTRO DE USUARIO", width=30 , height=2,
                                  command=lambda:cadastro_usuarios.cadastrar_usuarios(root), bg ="#e1e1e1")
btn_cadastrar_usuario.pack(pady=10)


btn_sair = tk.Button(root, text="SAIR", width=25, command=root.quit, fg="red")
btn_sair.pack(pady=20)


root.mainloop()
