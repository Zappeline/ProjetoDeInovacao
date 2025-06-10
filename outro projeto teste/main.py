import sqlite3
import tkinter as tk
from tkinter import messagebox
from hashlib import sha256

# ------------------ BANCO DE DADOS ------------------
conn = sqlite3.connect('plataforma.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    contato TEXT NOT NULL,
    senha_hash TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS imoveis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS semanas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imovel_id INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    disponivel BOOLEAN DEFAULT 1,
    usuario_id INTEGER,
    FOREIGN KEY(imovel_id) REFERENCES imoveis(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)''')

conn.commit()

# ------------------ FUNÇÕES ------------------
def hash_senha(senha):
    return sha256(senha.encode()).hexdigest()

def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    contato = entry_contato.get()
    senha = hash_senha(entry_senha.get())

    try:
        cursor.execute("INSERT INTO usuarios (nome, cpf, contato, senha_hash) VALUES (?, ?, ?, ?)",
                       (nome, cpf, contato, senha))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já cadastrado.")

def logar():
    cpf = entry_login_cpf.get()
    senha = hash_senha(entry_login_senha.get())
    cursor.execute("SELECT * FROM usuarios WHERE cpf=? AND senha_hash=?", (cpf, senha))
    usuario = cursor.fetchone()
    if usuario:
        abrir_perfil(usuario)
    else:
        messagebox.showerror("Erro", "Credenciais inválidas.")

def reservar_semana(usuario_id):
    def reservar():
        semana_id = entry_semana_id.get()
        cursor.execute("SELECT disponivel FROM semanas WHERE id=?", (semana_id,))
        result = cursor.fetchone()
        if result and result[0] == 1:
            cursor.execute("UPDATE semanas SET disponivel=0, usuario_id=? WHERE id=?", (usuario_id, semana_id))
            conn.commit()
            messagebox.showinfo("Sucesso", "Semana reservada com sucesso!")
            janela.destroy()
        else:
            messagebox.showerror("Erro", "Semana indisponível.")

    janela = tk.Toplevel(root)
    janela.title("Reservar Semana")
    tk.Label(janela, text="ID da Semana a reservar:").pack()
    entry_semana_id = tk.Entry(janela)
    entry_semana_id.pack()
    tk.Button(janela, text="Reservar", command=reservar).pack()

def listar_semanas():
    janela = tk.Toplevel(root)
    janela.title("Listagem de Semanas")
    cursor.execute("SELECT semanas.id, imoveis.nome, semanas.descricao, semanas.disponivel FROM semanas JOIN imoveis ON semanas.imovel_id = imoveis.id")
    for id_, imovel, desc, disp in cursor.fetchall():
        status = "Disponível" if disp else "Indisponível"
        tk.Label(janela, text=f"ID {id_} - {imovel} ({desc}) - {status}").pack()

def abrir_perfil(usuario):
    perfil = tk.Toplevel(root)
    perfil.title("Perfil")

    tk.Label(perfil, text=f"Nome: {usuario[1]}").pack()
    tk.Label(perfil, text=f"CPF: {usuario[2]}").pack()
    tk.Label(perfil, text=f"Contato: {usuario[3]}").pack()

    tk.Label(perfil, text="\nImóveis cadastrados:").pack()
    cursor.execute("SELECT * FROM imoveis")
    for imovel in cursor.fetchall():
        tk.Label(perfil, text=f"- {imovel[1]}").pack()

    tk.Button(perfil, text="Listar Semanas", command=listar_semanas).pack(pady=5)
    tk.Button(perfil, text="Reservar Semana", command=lambda: reservar_semana(usuario[0])).pack(pady=5)

# ------------------ INTERFACE TKINTER ------------------
root = tk.Tk()
root.title("Investimento Fracionado - Plataforma")

# Cadastro
tk.Label(root, text="Cadastro").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Nome").grid(row=1, column=0)
tk.Label(root, text="CPF").grid(row=2, column=0)
tk.Label(root, text="Contato").grid(row=3, column=0)
tk.Label(root, text="Senha").grid(row=4, column=0)

entry_nome = tk.Entry(root)
entry_cpf = tk.Entry(root)
entry_contato = tk.Entry(root)
entry_senha = tk.Entry(root, show="*")

entry_nome.grid(row=1, column=1)
entry_cpf.grid(row=2, column=1)
entry_contato.grid(row=3, column=1)
entry_senha.grid(row=4, column=1)

tk.Button(root, text="Cadastrar", command=cadastrar).grid(row=5, column=0, columnspan=2, pady=10)

# Login
tk.Label(root, text="Login").grid(row=6, column=0, columnspan=2)
tk.Label(root, text="CPF").grid(row=7, column=0)
tk.Label(root, text="Senha").grid(row=8, column=0)

entry_login_cpf = tk.Entry(root)
entry_login_senha = tk.Entry(root, show="*")

entry_login_cpf.grid(row=7, column=1)
entry_login_senha.grid(row=8, column=1)

tk.Button(root, text="Entrar", command=logar).grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
