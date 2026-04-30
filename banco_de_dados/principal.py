import tkinter as tk
from tkinter import ttk, messagebox
import categoria
import livro

# --- MENU PRINCIPAL (ROOT) ---
root = tk.Tk()
root.title("Menu Principal - Sistema de Biblioteca")
root.geometry("400x500")

# 1. Criar a barra de menu principal
barra_menu = tk.Menu(root)

# 2. Criar o menu "Categorias"
menu_categorias = tk.Menu(barra_menu, tearoff=0)
# Adicionando as opções dentro do menu Categorias
menu_categorias.add_command(label="Cadastrar Nova", command=lambda: categoria.abrir_form_categoria(root))
menu_categorias.add_command(label="Consultar Todas", command=lambda: categoria.abrir_consulta(root))
menu_categorias.add_separator() # Linha divisória
menu_categorias.add_command(label="Sair", command=root.quit)

# 3. Adicionar o menu Categorias à barra principal
barra_menu.add_cascade(label="Categorias", menu=menu_categorias)

# 5. Configurar a janela para usar esta barra de menu
root.config(menu=barra_menu)

tk.Label(root, text="GERENCIADOR BIBLIOTECA", font=("Arial", 14, "bold")).pack(pady=30)

btn_cadastrar = tk.Button(root, text="NOVO CADASTRO", width=25, height=2, 
                          command=lambda:categoria.abrir_cadastro(root), bg="#e1e1e1")
btn_cadastrar.pack(pady=10)

# O lambda cria um "adiamento". A função só roda no clique.
btn_consultar = tk.Button(
    root, 
    text="CONSULTAR LISTA", 
    command=lambda: categoria.abrir_consulta(root), 
    bg="#e1e1e1"
)
btn_consultar.pack(pady=10)

btn_cadastrar_livro = tk.Button(root, text="NOVO CADASTRO LIVRO", width=25, height=2, 
                          command=lambda:livro.abrir_cadastro_livro(root), bg="#e1e1e1")
btn_cadastrar_livro.pack(pady=10)

btn_sair = tk.Button(root, text="SAIR", width=25, command=root.quit, fg="red")
btn_sair.pack(pady=20)

root.mainloop()