import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import categoria_padrao
import lista_livro
import lista_autor
import lista_emprestimo



def abrir_opcao_lista(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar listas")
    janela_con.geometry("500x480") 

   


    btn_categoria = tk.Button(janela_con, text="LISTA DE CATEGORIAS", width=30, height=2, 
                          command=lambda:categoria_padrao.abrir_consulta(janela_con), bg="#e1e1e1")
    btn_categoria.pack(pady=10)

    btn_livro = tk.Button(janela_con, text="LISTA DE LIVROS", width=30, height=2, 
                          command=lambda:lista_livro.abrir_consulta_livro(janela_con), bg="#e1e1e1")
    btn_livro.pack(pady=10)

    btn_autor = tk.Button(janela_con, text="LISTA DE AUTORES", width=30 , height=2,
                                  command=lambda:lista_autor.abrir_consulta_autor(janela_con,), bg ="#e1e1e1")
    btn_autor.pack(pady=10)

    btn_emprestimo = tk.Button(janela_con, text="LISTA DE EMPRESTIMOS", width=30, height=2, 
                          command=lambda:lista_emprestimo.abrir_consulta_emprestimo(janela_con,), bg="#e1e1e1")
    btn_emprestimo.pack(pady=10)

    btn_cadastrar_emprestimo = tk.Button(janela_con, text="LISTA DE MULTAS", width=30 , height=2,
                                  command=lambda:emprestimo.abrir_cadastro_emprestimo(janela_con), bg ="#e1e1e1")
    btn_cadastrar_emprestimo.pack(pady=10)

    