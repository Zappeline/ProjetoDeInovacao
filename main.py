import tkinter as tk
from tkinter import ttk, messagebox
from models.Imoveis import Imoveis
from models.Usuarios import Usuarios
from models.DBService import banco_dados

class Sistemainvestimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Investimento Fracionado")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # --- Container principal para todas as telas ---
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # --- Dicionário para armazenar todas as telas ---
        self.telas = {}

        # --- Criação de todas as frames (telas) do sistema ---
        for F in (
            "tela_login", "tela_cadastro", "tela_principal", "tela_perfil",
            "tela_atualizar_cadastro", "tela_investimento", "tela_imovel1",
            "tela_imovel2", "tela_listar_imovel1", "tela_listar_imovel2", "tela_saibamais"
        ):
            frame = tk.Frame(self.container)
            self.telas[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # --- Configuração inicial das telas ---
        self.configurar_tela_login()
        self.configurar_tela_cadastro()
        self.configurar_tela_principal()

        # --- Inicia mostrando a tela de login ---
        self.mostrar_tela("tela_principal")

    def mostrar_tela(self, nome_tela):
        """Eleva a tela desejada para o topo, tornando-a visível."""
        tela = self.telas[nome_tela]
        tela.tkraise()

    def configurar_tela_login(self):
        """Configura os widgets e o layout da tela de login."""
        tela_login = self.telas["tela_login"]
        
        # Frame central para organizar os elementos de login
        frame_login = tk.Frame(tela_login)
        frame_login.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_login, text="Login", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame_login, text="CPF:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        self.cpf = tk.Entry(frame_login, width=20)
        self.cpf.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame_login, text="Senha:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
        self.senha = tk.Entry(frame_login, width=20, show="*")
        self.senha.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        btn_logar = tk.Button(frame_login, text="Entrar", command=lambda: self.mostrar_tela("tela_principal"))
        btn_logar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        
        btn_cadastrar = tk.Button(frame_login, text="Não tem conta? Cadastre-se", command=lambda: self.mostrar_tela("tela_cadastro"))
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

    def configurar_tela_cadastro(self):
        """Configura os widgets e o layout da tela de cadastro."""
        tela_cadastro = self.telas["tela_cadastro"]
        
        # Frame central para organizar os elementos de cadastro
        frame_cadastro = tk.Frame(tela_cadastro)
        frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")
        
        titulo = tk.Label(frame_cadastro, text="Cadastro de Novo Usuário", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame_cadastro, text="Nome Completo:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        self.nome_cadastro = tk.Entry(frame_cadastro, width=25)
        self.nome_cadastro.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame_cadastro, text="CPF:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
        self.cpf_cadastro = tk.Entry(frame_cadastro, width=25)
        self.cpf_cadastro.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame_cadastro, text="Senha:").grid(row=3, column=0, sticky="e", pady=5, padx=5)
        self.senha_cadastro = tk.Entry(frame_cadastro, width=25, show="*")
        self.senha_cadastro.grid(row=3, column=1, sticky="w", pady=5, padx=5)
        
        btn_cadastrar = tk.Button(frame_cadastro, text="Finalizar Cadastro", command=self.cadastrar_usuario)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        btn_voltar = tk.Button(frame_cadastro, text="Voltar para Login", command=lambda: self.mostrar_tela("tela_login"))
        btn_voltar.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")
    
   
    def configurar_tela_principal(self):
        """Configura os widgets e o layout da tela principal."""
        tela_principal = self.telas["tela_principal"]
        
        # Frame central para organizar os elementos da tela principal
        frame_principal = tk.Frame(tela_principal)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_principal, text="Investfácil", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        btn_perfil = tk.Button(frame_principal, text="Meu Perfil", command=lambda: self.mostrar_tela("tela_perfil"))
        btn_perfil.grid(row=1, column=0, pady=5, padx=5)

        btn_investimento = tk.Button(frame_principal, text="Investimentos", command=lambda: self.mostrar_tela("tela_investimento"))
        btn_investimento.grid(row=1, column=1, pady=5, padx=5)
        
        btn_saibamais = tk.Button(frame_principal, text="Saiba Mais", command=self.saiba_mais)
        btn_saibamais.grid(row=1, column=2, pady=5, padx=5)

        btn_sair = tk.Button(frame_principal, text="Sair", command=self.root.quit)
        btn_sair.grid(row=2, column=0, columnspan=2, pady=10)
    
    def cadastrar_usuario(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        contato = self.contato.get()
        
        if not nome or not cpf or not contato:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        try:
            novo_usuario = Usuarios.cadastrar_usuarios(nome, cpf, contato)
            messagebox.showinfo("Sucesso", f"Usuário {novo_usuario.nome} cadastrado com sucesso!")
            self.mostrar_tela(self.tela_principal)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_cadastro(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        contato = self.contato.get()
        
        if not nome or not cpf or not contato:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        try:
            usuario = Usuarios.atualizar_usuario(contato)
            messagebox.showinfo("Sucesso", f"Contato do usuário {usuario.nome} atualizado com sucesso!")
            self.mostrar_tela(self.tela_perfil)
        except Exception as e:
            messagebox.showerror("Erro", str(e))


    def saiba_mais(self):
        messagebox.showinfo("Acredita que ter um imóvel de luxo está fora do seu alcance? Pense novamente!" \
        "O investimento fracionado oferece a você a oportunidade de ser proprietário de um pedacinho do paraíso." \
        "São 52 semanas no ano, e sua fatia te dá o direito de uso ou de locação." \
        "Quer usar sua semana para relaxar? À vontade! Quer rentabilizar?" \
        "Alugue sua semana de forma prática e segura, transformando seu investimento em uma fonte de renda." \
        "É a porta de entrada para um mercado exclusivo, com a flexibilidade e a rentabilidade que você sempre buscou.")
        


        
    """def tela_listar_semana_imovel1(self, root):
        self.root = root
        self.root.title("InvestFacil - Imóveis Fracionados")
        self.root.geometry("600x400")

        self.imovel = banco_dados["imovel"]
        self.usuarios = banco_dados["usuarios"]

        self.usuario_atual = self.usuarios[0]

        self.label = ttk.Label(root, text="Semanas disponíveis: ZenithPlace")
        self.label.pack(pady=10)

        self.lista = tk.Listbox(root, width=80, height=15)
        self.lista.pack()

        self.atualizar_lista()

        self.botao_comprar = ttk.Button(root, text="Comprar Semana Selecionada", command=self.comprar_semana)
        self.botao_comprar.pack(pady=10)

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for semana in self.imovel.semanas:
            status = f"{semana.numero} - R${semana.preco:,.2f} - {'Disponível' if semana.dono is None else f'Ocupada por {semana.dono.nome}'}"
            self.lista.insert(tk.END, status)

    def comprar_semana(self):
        selecionado = self.lista.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma semana.")
            return

        index = selecionado[0]
        semana = self.imovel.semanas[index]

        if semana.dono is not None:
            messagebox.showerror("Erro", "Semana já está ocupada.")
            return

        semana.dono = self.usuario_atual
        self.usuario_atual.semanas.append(semana)
        messagebox.showinfo("Sucesso", f"Semana {semana.numero} adquirida!")
        self.atualizar_lista()"""    
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Sistemainvestimento(root)
    root.mainloop()