import tkinter as tk
from tkinter import ttk, messagebox
from models.Imoveis import Imoveis

"""from models.Usuarios import Usuarios"""
"""from models.DBService import banco_dados
"""

class Sistemainvestimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Investimento Fracionado")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

      
        self.telas = {}


        for telas in (
            "tela_login", "tela_cadastro", "tela_principal", "tela_perfil",
            "tela_investimento", "tela_imovel1", "tela_imovel2", 
            "tela_listar_imovel1", "tela_listar_imovel2"
        ):
            frame = tk.Frame(self.container)
            self.telas[telas] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # --- Configuração inicial das telas ---
        self.configurar_tela_login()
        self.configurar_tela_cadastro()
        self.configurar_tela_principal()
        self.configurar_tela_perfil()
        self.configurar_tela_investimento()
        self.configurar_tela_imovel1()
        self.configurar_tela_imovel2()
        self.configurar_tela_listar_imovel1()
        self.configurar_tela_listar_imovel2()
        
        # --- Inicia mostrando a tela de login ---
        self.mostrar_tela("tela_principal")

    def mostrar_tela(self, nome_tela):
        tela = self.telas[nome_tela]
        tela.tkraise()

    def configurar_tela_login(self):
        tela_login = self.telas["tela_login"]
        frame_login = tk.Frame(tela_login)
        frame_login.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_login, text="Login", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame_login, text="CPF:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        self.cpf_login = tk.Entry(frame_login, width=20)
        self.cpf_login.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame_login, text="Senha:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
        self.senha_login = tk.Entry(frame_login, width=20, show="*")
        self.senha_login.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        btn_logar = tk.Button(frame_login, text="Entrar", command=lambda: self.mostrar_tela("tela_principal"))
        btn_logar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        btn_cadastrar = tk.Button(frame_login, text="Não tem conta? Cadastre-se agora!", command=lambda: self.mostrar_tela("tela_cadastro"))
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

    def configurar_tela_cadastro(self):
        tela_cadastro = self.telas["tela_cadastro"]
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
        tela_principal = self.telas["tela_principal"]
        frame_principal = tk.Frame(tela_principal)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_principal, text="INVESTFACIL", font=("Arial", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=20)

        btn_perfil = tk.Button(frame_principal, text="Meu Perfil", width=15, command=lambda: self.mostrar_tela("tela_perfil"))
        btn_perfil.grid(row=1, column=0, pady=10, padx=10)

        btn_investimento = tk.Button(frame_principal, text="Investimentos", width=15, command=lambda: self.mostrar_tela("tela_investimento"))
        btn_investimento.grid(row=1, column=1, pady=10, padx=10)
        
        btn_saibamais = tk.Button(frame_principal, text="Saiba Mais", width=15, command=self.saiba_mais)
        btn_saibamais.grid(row=1, column=2, pady=10, padx=10)

        btn_sair = tk.Button(frame_principal, text="Sair", command=lambda: self.mostrar_tela("tela_login"))
        btn_sair.grid(row=2, column=0, columnspan=3, pady=20)

    def configurar_tela_perfil(self):
        tela_perfil = self.telas["tela_perfil"]
        frame_perfil = tk.Frame(tela_perfil)
        frame_perfil.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_perfil, text="Meu Perfil", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        label_info = tk.Label(frame_perfil, text="Investimentos", font=("Arial", 10))
        label_info.pack(pady=20, padx=20)

        btn_voltar = tk.Button(frame_perfil, text="Voltar", command=lambda: self.mostrar_tela("tela_principal"))
        btn_voltar.pack(pady=10)

    def configurar_tela_investimento(self):
        tela_investimento = self.telas["tela_investimento"]
        frame_investimento = tk.Frame(tela_investimento)
        frame_investimento.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_investimento, text="Escolha o Empreendimento", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        btn_imovel1 = tk.Button(frame_investimento, text="Imóvel 1 - ZenithPlace", width=30, command=lambda: self.mostrar_tela("tela_imovel1"))
        btn_imovel1.pack(pady=10, padx=20)

        btn_imovel2 = tk.Button(frame_investimento, text="Imóvel 2 - Topázio Imperial Hotel", width=30, command=lambda: self.mostrar_tela("tela_imovel2"))
        btn_imovel2.pack(pady=10, padx=20)

        btn_voltar = tk.Button(frame_investimento, text="Voltar", command=lambda: self.mostrar_tela("tela_principal"))
        btn_voltar.pack(pady=20)

    def configurar_tela_imovel1(self):
        tela_imovel1 = self.telas["tela_imovel1"]
        frame_imovel1 = tk.Frame(tela_imovel1)
        frame_imovel1.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_imovel1, text="ZenithPlace", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        descricao = tk.Label(frame_imovel1, text="Descrição", justify="center")
        descricao.pack(pady=10, padx=20)

        btn_listar = tk.Button(frame_imovel1, text="Listar Semanas Disponíveis", command=lambda: self.mostrar_tela("tela_listar_imovel1"))
        btn_listar.pack(pady=20)

        btn_voltar = tk.Button(frame_imovel1, text="Voltar", command=lambda: self.mostrar_tela("tela_investimento"))
        btn_voltar.pack(pady=10)

    def configurar_tela_imovel2(self):
        tela_imovel2 = self.telas["tela_imovel2"]
        frame_imovel2 = tk.Frame(tela_imovel2)
        frame_imovel2.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame_imovel2, text="Topázio Imperial Hotel", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        descricao = tk.Label(frame_imovel2, text="Descrição ho", justify="center")
        descricao.pack(pady=10, padx=20)

        btn_listar = tk.Button(frame_imovel2, text="Listar Semanas Disponíveis", command=lambda: self.mostrar_tela("tela_listar_imovel2"))
        btn_listar.pack(pady=20)

        btn_voltar = tk.Button(frame_imovel2, text="Voltar", command=lambda: self.mostrar_tela("tela_investimento"))
        btn_voltar.pack(pady=10)

    def configurar_tela_listar_imovel1(self):
        
        tela_listar = self.telas["tela_listar_imovel1"]
        frame_listar = tk.Frame(tela_listar, pady=20)
        frame_listar.pack(fill="both", expand=True)

        titulo = tk.Label(frame_listar, text="Semanas Disponíveis - PASTELZINHO DE CHOCOLATE", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        
        colunas = ('semana', 'periodo', 'valor')
        tabela = ttk.Treeview(frame_listar, columns=colunas, show='headings')
        tabela.heading('semana', text='Semana Nº')
        tabela.heading('periodo', text='Período')
        tabela.heading('valor', text='Valor da Cota (R$)')
        
        
        semanas_imovel1 = [
            ('15', '12/04 - 19/04', '15.000,00'),
            ('22', '31/05 - 07/06', '18.000,00'),
            ('35', '30/08 - 06/09', '22.000,00')
        ]
        for semana in semanas_imovel1:
            tabela.insert('', 'end', values=semana)
        
        tabela.pack(pady=10, padx=20, fill="both", expand=True)

        btn_voltar = tk.Button(frame_listar, text="Voltar", command=lambda: self.mostrar_tela("tela_imovel1"))
        btn_voltar.pack(pady=10)

    def configurar_tela_listar_imovel2(self):
        tela_listar = self.telas["tela_listar_imovel2"]
        frame_listar = tk.Frame(tela_listar, pady=20)
        frame_listar.pack(fill="both", expand=True)

        titulo = tk.Label(frame_listar, text="Semanas Disponíveis - Pastelzinho quentinho", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        # NEM SEI COMO FAZER ISSO HAHAHAHHAHAHH
        colunas = ('semana', 'periodo', 'valor')
        tabela = ttk.Treeview(frame_listar, columns=colunas, show='headings')
        tabela.heading('semana', text='Semana Nº')
        tabela.heading('periodo', text='Período')
        tabela.heading('valor', text='Valor da Cota (R$)')
        
        #MUDA BURRO HAHAHAHAHAHHAHAH
        semanas_imovel2 = [
            ('28', '12/07 - 19/07', '35.000,00'),
            ('29', '19/07 - 26/07', '35.000,00'),
            ('41', '11/10 - 18/10', '28.000,00')
        ]
        for semana in semanas_imovel2:
            tabela.insert('', 'end', values=semana)
        
        tabela.pack(pady=10, padx=20, fill="both", expand=True)

        btn_voltar = tk.Button(frame_listar, text="Voltar", command=lambda: self.mostrar_tela("tela_imovel2"))
        btn_voltar.pack(pady=10)

    def cadastrar_usuario(self):
        
        nome = self.nome_cadastro.get()
        cpf = self.cpf_cadastro.get()
        senha = self.senha_cadastro.get()
        
        if not nome or not cpf or not senha:
            messagebox.showerror("Erro de Cadastro", "Todos os campos são obrigatórios.")
            return
        
        try:
            
            # novo_usuario = Usuarios.cadastrar_usuarios(nome, cpf, contato)
            
           
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
            self.mostrar_tela("tela_login") 
        except Exception as e:
            messagebox.showerror("Erro Inesperado", str(e))

    def atualizar_cadastro(self):
        
        pass

    def saiba_mais(self):
        messagebox.showinfo("O que é Investimento Fracionado?",
        "Acredita que ter um imóvel de luxo está fora do seu alcance? Pense novamente!\n\n"
        "O investimento fracionado oferece a você a oportunidade de ser proprietário de um pedacinho do paraíso. "
        "São 52 semanas no ano, e sua fatia te dá o direito de uso ou de locação.\n\n"
        "Quer usar sua semana para relaxar? À vontade! Quer rentabilizar? "
        "Alugue sua semana de forma prática e segura, transformando seu investimento em uma fonte de renda.\n\n"
        "É a porta de entrada para um mercado exclusivo, com a flexibilidade e a rentabilidade que você sempre buscou.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Sistemainvestimento(root)
    root.mainloop()

        
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
        

