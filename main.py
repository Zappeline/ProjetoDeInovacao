import tkinter as tk
from tkinter import ttk, messagebox
from db_operations import (
    criar_usuario_db, verificar_login_db, atualizar_contato_usuario_db,
    get_semanas_disponiveis, comprar_semana_db, get_transacoes_usuario_db,
    inicializar_dados_imoveis, desfazer_compra_semana_db
)
from validador import is_cpf_valido, is_nome_valido, is_contato_valido

class Sistemainvestimento:
    def __init__(self, root):
        self.root = root
        self.root.title("INVESTFACIL - Sistema de Investimento Fracionado")
        self.root.geometry("900x650") 
        self.root.minsize(800, 600) 
        self.root.resizable(True, True)
        self.current_user = None
        self.setup_styles()
        self.container = ttk.Frame(root, style="Main.TFrame")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.telas = {}
        telas_a_criar = (
            "tela_login", "tela_cadastro", "tela_principal", "tela_perfil",
            "tela_investimento", "tela_imovel1", "tela_imovel2", "tela_imovel3",
            "tela_listar_imovel1", "tela_listar_imovel2", "tela_listar_imovel3"
        )

        for nome_tela in telas_a_criar:
            frame = ttk.Frame(self.container, style="Content.TFrame")
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.configurar_todas_as_telas()
        self.mostrar_tela("tela_login")
        inicializar_dados_imoveis() 

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        
        self.primary_color = "#4CAF50" # verde
        self.secondary_color = "#2196F3" # azul
        self.accent_color = "#FFC107" # laranja
        self.background_color = "#f0f2f5" # azul claro
        self.card_background = "#ffffff" # branco
        self.light_text = "#ffffff" # branco
        self.dark_text = "#333333" # cinza
        self.border_color = "#e0e0e0" # cinza claro
        self.error_color = "#F44336" # vermelho
        self.info_color = "#607D8B" # blue

        
        style.configure("Main.TFrame", background=self.background_color)
        style.configure("Content.TFrame", background=self.background_color)
        style.configure("Card.TFrame", background=self.card_background, relief="flat", borderwidth=1, bordercolor=self.border_color)
        style.map("Card.TFrame",
            background=[('active', self.card_background)], 
            bordercolor=[('active', self.border_color)]
        )

        
        style.configure("TLabel", background=self.background_color, foreground=self.dark_text, font=("Segoe UI", 11))
        style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"), foreground=self.primary_color, background=self.background_color)
        style.configure("Subtitle.TLabel", font=("Segoe UI", 16, "bold"), foreground=self.dark_text, background=self.background_color)
        style.configure("Heading.TLabel", font=("Segoe UI", 12, "bold"), foreground=self.dark_text, background=self.card_background)
        style.configure("Info.TLabel", font=("Segoe UI", 11), foreground=self.dark_text, background=self.card_background)
        style.configure("SmallInfo.TLabel", font=("Segoe UI", 9), foreground="#666666", background=self.card_background)

        
        style.configure("TEntry", fieldbackground=self.card_background, borderwidth=1, relief="solid", font=("Segoe UI", 11), padding=5)
        style.map("TEntry", fieldbackground=[('focus', '#e8f0fe')]) # Subtle highlight on focus

        
        style.configure("TButton",
            font=("Segoe UI", 11, "bold"),
            background=self.primary_color, foreground=self.light_text,
            relief="flat", borderwidth=0, padding=(15, 10),
            focusthickness=0
        )
        style.map("TButton",
            background=[('active', self.secondary_color), ('pressed', self.dark_text)],
            foreground=[('active', self.light_text), ('pressed', self.light_text)]
        )
        style.configure("Primary.TButton", background=self.primary_color, foreground=self.light_text)
        style.configure("Secondary.TButton", background=self.secondary_color, foreground=self.light_text)
        style.configure("Accent.TButton", background=self.accent_color, foreground=self.dark_text) 
        style.configure("Danger.TButton", background=self.error_color, foreground=self.light_text)
        style.configure("Info.TButton", background=self.info_color, foreground=self.light_text)

        
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background=self.border_color, foreground=self.dark_text, padding=(5, 8))
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=28, background=self.card_background, fieldbackground=self.card_background, foreground=self.dark_text, borderwidth=0)
        style.map("Treeview", background=[('selected', self.secondary_color)], foreground=[('selected', self.light_text)])

        
        style.configure("Vertical.TScrollbar", troughcolor=self.background_color, background=self.secondary_color, borderwidth=0, arrowsize=15)
        style.map("Vertical.TScrollbar",
            background=[('active', self.primary_color)]
        )


    def configurar_todas_as_telas(self):
        self.configurar_tela_login()
        self.configurar_tela_cadastro()
        self.configurar_tela_principal()
        self.configurar_tela_perfil() 
        self.configurar_tela_investimento()
        self.configurar_tela_imovel1()
        self.configurar_tela_imovel2()
        self.configurar_tela_imovel3()

    def mostrar_tela(self, nome_tela):
        tela = self.telas[nome_tela]
        tela.tkraise()
        if nome_tela == "tela_perfil":
            self.atualizar_tela_perfil()
        elif nome_tela == "tela_listar_imovel1":
            self.configurar_tela_listar_imovel1()
        elif nome_tela == "tela_listar_imovel2":
            self.configurar_tela_listar_imovel2()
        elif nome_tela == "tela_listar_imovel3":
            self.configurar_tela_listar_imovel3()

    def configurar_tela_login(self):
        tela_login = self.telas["tela_login"]
        frame_login = ttk.Frame(tela_login, style="Card.TFrame", padding=40)
        frame_login.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame_login, text="Bem-vindo ao INVESTFACIL", style="Title.TLabel", background=self.card_background, foreground=self.primary_color).grid(row=0, column=0, columnspan=2, pady=(0, 25))
        ttk.Label(frame_login, text="Faça Login para Continuar", style="Subtitle.TLabel", background=self.card_background, foreground=self.dark_text).grid(row=1, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame_login, text="CPF:", style="Info.TLabel").grid(row=2, column=0, sticky="e", pady=10, padx=10)
        self.cpf_login_entry = ttk.Entry(frame_login, width=35)
        self.cpf_login_entry.grid(row=2, column=1, sticky="w", pady=10, padx=10)

        ttk.Label(frame_login, text="Senha:", style="Info.TLabel").grid(row=3, column=0, sticky="e", pady=10, padx=10)
        self.senha_login_entry = ttk.Entry(frame_login, width=35, show="*")
        self.senha_login_entry.grid(row=3, column=1, sticky="w", pady=10, padx=10)

        ttk.Button(frame_login, text="Entrar", command=self.processar_login, style="Primary.TButton").grid(row=4, column=0, columnspan=2, pady=(25, 10), sticky="ew")

        ttk.Button(frame_login, text="Não tem conta? Cadastre-se!", command=lambda: self.mostrar_tela("tela_cadastro"),
                                  style="Secondary.TButton").grid(row=5, column=0, columnspan=2, pady=(5, 0), sticky="ew")

    def configurar_tela_cadastro(self):
        tela_cadastro = self.telas["tela_cadastro"]
        frame_cadastro = ttk.Frame(tela_cadastro, style="Card.TFrame", padding=40)
        frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame_cadastro, text="Crie Sua Conta Grátis", style="Title.TLabel", background=self.card_background, foreground=self.primary_color).grid(row=0, column=0, columnspan=2, pady=(0, 25))

        ttk.Label(frame_cadastro, text="Nome Completo:", style="Info.TLabel").grid(row=1, column=0, sticky="e", pady=8, padx=10)
        self.nome_cadastro_entry = ttk.Entry(frame_cadastro, width=35)
        self.nome_cadastro_entry.grid(row=1, column=1, sticky="w", pady=8, padx=10)

        ttk.Label(frame_cadastro, text="CPF:", style="Info.TLabel").grid(row=2, column=0, sticky="e", pady=8, padx=10)
        self.cpf_cadastro_entry = ttk.Entry(frame_cadastro, width=35)
        self.cpf_cadastro_entry.grid(row=2, column=1, sticky="w", pady=8, padx=10)

        ttk.Label(frame_cadastro, text="Contato (Email):", style="Info.TLabel").grid(row=3, column=0, sticky="e", pady=8, padx=10)
        self.contato_cadastro_entry = ttk.Entry(frame_cadastro, width=35)
        self.contato_cadastro_entry.grid(row=3, column=1, sticky="w", pady=8, padx=10)

        ttk.Label(frame_cadastro, text="Senha:", style="Info.TLabel").grid(row=4, column=0, sticky="e", pady=8, padx=10)
        self.senha_cadastro_entry = ttk.Entry(frame_cadastro, width=35, show="*")
        self.senha_cadastro_entry.grid(row=4, column=1, sticky="w", pady=8, padx=10)
        ttk.Button(frame_cadastro, text="Finalizar Cadastro", command=self.processar_cadastro, style="Accent.TButton").grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=(20, 10))

        ttk.Button(frame_cadastro, text="Voltar para Login", command=lambda: self.mostrar_tela("tela_login"),
                                     style="Info.TButton").grid(row=6, column=0, columnspan=2, pady=(0, 0), sticky="ew")

    def processar_login(self):
        cpf = self.cpf_login_entry.get()
        senha = self.senha_login_entry.get()

        if not cpf or not senha:
            messagebox.showerror("Erro de Login", "CPF e Senha são obrigatórios.")
            return

        if not is_cpf_valido(cpf):
            messagebox.showerror("Erro de Login", "O CPF inserido não é válido. Verifique o formato e os dígitos.")
            return

        usuario = verificar_login_db(cpf, senha)
        if usuario:
            self.current_user = usuario
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.mostrar_tela("tela_principal")
            self.atualizar_tela_principal()
            self.cpf_login_entry.delete(0, tk.END)
            self.senha_login_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro de Login", "CPF ou senha inválidos.")

    def processar_cadastro(self):
        nome = self.nome_cadastro_entry.get()
        cpf = self.cpf_cadastro_entry.get()
        contato = self.contato_cadastro_entry.get()
        senha = self.senha_cadastro_entry.get()
        valido, msg = is_nome_valido(nome)
        if not valido:
            messagebox.showerror("Erro de Cadastro", msg)
            return

        if not is_cpf_valido(cpf):
            messagebox.showerror("Erro de Cadastro", "O CPF inserido não é válido. Verifique o formato e os dígitos.")
            return
            
        valido, msg = is_contato_valido(contato)
        if not valido:
            messagebox.showerror("Erro de Cadastro", msg)
            return
        novo_usuario, mensagem = criar_usuario_db(nome, cpf, contato, senha)

        if novo_usuario:
            messagebox.showinfo("Sucesso", mensagem)
            self.mostrar_tela("tela_login")
            self.nome_cadastro_entry.delete(0, tk.END)
            self.cpf_cadastro_entry.delete(0, tk.END)
            self.contato_cadastro_entry.delete(0, tk.END)
            self.senha_cadastro_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro de Cadastro", mensagem)

    def configurar_tela_principal(self):
        tela_principal = self.telas["tela_principal"]
        frame_principal = ttk.Frame(tela_principal, style="Card.TFrame", padding=50)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame_principal, text="INVESTFACIL", style="Title.TLabel", background=self.card_background, foreground=self.primary_color).grid(row=0, column=0, columnspan=3, pady=(0, 30))

        button_width = 25 

        ttk.Button(frame_principal, text="Meu Perfil", style="Primary.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_perfil")).grid(row=1, column=0, pady=15, padx=15)
        ttk.Button(frame_principal, text="Investimentos", style="Primary.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_investimento")).grid(row=1, column=1, pady=15, padx=15)
        ttk.Button(frame_principal, text="Saiba Mais", style="Primary.TButton", width=button_width, command=self.saiba_mais).grid(row=1, column=2, pady=15, padx=15)

        ttk.Button(frame_principal, text="Sair", style="Danger.TButton", width=button_width, command=self.fazer_logout).grid(row=2, column=0, columnspan=3, pady=(30,0))

    def fazer_logout(self):
        self.current_user = None
        messagebox.showinfo("Logout", "Você foi desconectado com sucesso.")
        self.mostrar_tela("tela_login")

    def configurar_tela_perfil(self):
        tela_perfil = self.telas["tela_perfil"]
        for widget in tela_perfil.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(tela_perfil, style="Content.TFrame", padding=20)
        main_frame.pack(fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=0) 
        main_frame.grid_rowconfigure(1, weight=0) 
        main_frame.grid_rowconfigure(2, weight=1) 
        main_frame.grid_rowconfigure(3, weight=0) 
        main_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(main_frame, text="Meu Perfil de Investidor", style="Title.TLabel", background=self.background_color, foreground=self.primary_color).grid(row=0, column=0, pady=(0, 25), sticky="ew")

        if self.current_user:
            info_frame = ttk.LabelFrame(main_frame, text="Suas Informações", style="Card.TFrame", padding=20)
            info_frame.grid(row=1, column=0, pady=15, padx=20, sticky="ew")
            info_frame.grid_columnconfigure(1, weight=1)

            ttk.Label(info_frame, text="Nome:", style="Heading.TLabel").grid(row=0, column=0, sticky="w", pady=5, padx=5)
            ttk.Label(info_frame, text=self.current_user.nome, style="Info.TLabel").grid(row=0, column=1, sticky="w", pady=5, padx=5)

            ttk.Label(info_frame, text="CPF:", style="Heading.TLabel").grid(row=1, column=0, sticky="w", pady=5, padx=5)
            ttk.Label(info_frame, text=self.current_user.cpf, style="Info.TLabel").grid(row=1, column=1, sticky="w", pady=5, padx=5)

            ttk.Label(info_frame, text="Contato (Email):", style="Heading.TLabel").grid(row=2, column=0, sticky="w", pady=10, padx=5)
            self.contato_perfil_entry = ttk.Entry(info_frame, width=45)
            self.contato_perfil_entry.insert(0, self.current_user.contato)
            self.contato_perfil_entry.grid(row=2, column=1, sticky="ew", padx=5)
            ttk.Button(info_frame, text="Atualizar Contato", command=self.atualizar_contato, style="Secondary.TButton", width=20).grid(row=2, column=2, padx=10, sticky="e")

            compras_frame = ttk.LabelFrame(main_frame, text="Minhas Semanas Adquiridas", style="Card.TFrame", padding=20)
            compras_frame.grid(row=2, column=0, pady=25, padx=20, sticky="nsew")
            compras_frame.grid_rowconfigure(0, weight=1)
            compras_frame.grid_columnconfigure(0, weight=1)

            colunas = ('id', 'imovel', 'semana_numero', 'periodo', 'valor_pago', 'data_compra')
            self.tabela_compras = ttk.Treeview(compras_frame, columns=colunas, show='headings', style="Treeview")

            self.tabela_compras.heading('id', text='ID', anchor='center')
            self.tabela_compras.heading('imovel', text='Imóvel', anchor='w')
            self.tabela_compras.heading('semana_numero', text='Semana Nº', anchor='center')
            self.tabela_compras.heading('periodo', text='Período de Uso', anchor='center')
            self.tabela_compras.heading('valor_pago', text='Valor Pago (R$)', anchor='e')
            self.tabela_compras.heading('data_compra', text='Data da Compra', anchor='center')

            self.tabela_compras.column('id', width=60, anchor='center', stretch=False)
            self.tabela_compras.column('imovel', width=250, anchor='w')
            self.tabela_compras.column('semana_numero', width=90, anchor='center')
            self.tabela_compras.column('periodo', width=150, anchor='center')
            self.tabela_compras.column('valor_pago', width=130, anchor='e')
            self.tabela_compras.column('data_compra', width=150, anchor='center')

            self.tabela_compras.grid(row=0, column=0, sticky="nsew", pady=(0, 15), padx=(0, 5))

            scrollbar = ttk.Scrollbar(compras_frame, orient="vertical", command=self.tabela_compras.yview, style="Vertical.TScrollbar")
            scrollbar.grid(row=0, column=1, sticky="ns", pady=(0, 15))
            self.tabela_compras.configure(yscrollcommand=scrollbar.set)

            ttk.Button(compras_frame, text="Disponibilizar Semana para Venda",
                                          command=self.desfazer_compra_semana,
                                          style="Danger.TButton", width=30).grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="ew")
            self.atualizar_tabela_compras()

        else:
            ttk.Label(main_frame, text="Nenhum usuário logado. Por favor, faça login.",
                      font=("Segoe UI", 12), background=self.background_color, foreground=self.dark_text).grid(row=2, column=0, pady=50, sticky="nsew")
        ttk.Button(main_frame, text="Voltar ao Painel", command=lambda: self.mostrar_tela("tela_principal"),
                               style="Info.TButton", width=30).grid(row=3, column=0, pady=(30, 0), sticky="ew")


    def atualizar_tela_perfil(self):
        self.configurar_tela_perfil()
    def atualizar_contato(self):
        if not self.current_user:
            messagebox.showerror("Erro", "Nenhum usuário logado.")
            return

        novo_contato = self.contato_perfil_entry.get()
        if not novo_contato:
            messagebox.showerror("Erro", "O contato não pode ser vazio.")
            return

        sucesso, mensagem = atualizar_contato_usuario_db(self.current_user.id, novo_contato)
        if sucesso:
            self.current_user.contato = novo_contato
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)

    def atualizar_tabela_compras(self):
        for item in self.tabela_compras.get_children():
            self.tabela_compras.delete(item)

        if self.current_user:
            transacoes = get_transacoes_usuario_db(self.current_user.id)
            for transacao in transacoes:
                imovel_nome = ""
                semana_periodo = ""
                semana_numero = ""
                semana_id = ""

                if transacao.semana and transacao.semana.imovel:
                    imovel_geral = {
                        1: "ZenithPlace",
                        2: "Topázio Imperial Hotel",
                        3: "Petra Palace"
                    }
                    imovel_nome = imovel_geral.get(transacao.semana.imovel.id, transacao.semana.imovel.endereco)
                    semana_periodo = transacao.semana.periodo
                    semana_numero = transacao.semana.numero_semana
                    semana_id = transacao.semana.id

                self.tabela_compras.insert('', 'end', values=(
                    semana_id,
                    imovel_nome,
                    semana_numero,
                    semana_periodo,
                    f"{transacao.valor_pago:,.2f}".replace('.', ','),
                    transacao.data_compra
                ), iid=str(semana_id))

    def desfazer_compra_semana(self):
        if not self.current_user:
            messagebox.showerror("Erro", "Você precisa estar logado.")
            return

        selected_item = self.tabela_compras.selection()
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione uma semana na tabela para disponibilizá-la.")
            return
        semana_id_str = selected_item[0]
        try:
            semana_id = int(semana_id_str)
        except ValueError:
            messagebox.showerror("Erro", "Não foi possível identificar a semana selecionada.")
            return
        row_values = self.tabela_compras.item(selected_item[0], 'values')
        imovel_nome = row_values[1]
        semana_numero = row_values[2]
        semana_periodo = row_values[3]

        confirm = messagebox.askyesno(
            "Confirmar Disponibilização",
            f"Você tem certeza que deseja disponibilizar a Semana Nº ({semana_periodo}) do imóvel {imovel_nome} para venda novamente?\n"
            "Esta ação é irreversível e removerá seu registro de compra."
        )

        if confirm:
            sucesso, mensagem = desfazer_compra_semana_db(self.current_user.id, semana_id)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.atualizar_tabela_compras()
                self.configurar_tela_listar_imovel1()
                self.configurar_tela_listar_imovel2()
                self.configurar_tela_listar_imovel3()

            else:
                messagebox.showerror("Erro", mensagem)

    def configurar_tela_investimento(self):
        tela_investimento = self.telas["tela_investimento"]
        frame_investimento = ttk.Frame(tela_investimento, style="Card.TFrame", padding=40)
        frame_investimento.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame_investimento, text="Explore Nossos Empreendimentos", style="Subtitle.TLabel", background=self.card_background, foreground=self.dark_text).pack(pady=(0, 20))

        button_width = 35

        ttk.Button(frame_investimento, text="Imóvel 1 - ZenithPlace", style="Primary.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_imovel1")).pack(pady=10, padx=20)
        ttk.Button(frame_investimento, text="Imóvel 2 - Topázio Imperial Hotel", style="Primary.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_imovel2")).pack(pady=10, padx=20)
        ttk.Button(frame_investimento, text="Imóvel 3 - Petra Palace", style="Primary.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_imovel3")).pack(pady=10, padx=20)
        ttk.Button(frame_investimento, text="Voltar ao Painel", style="Info.TButton", width=button_width, command=lambda: self.mostrar_tela("tela_principal")).pack(pady=(30,0))

    def configurar_tela_imovel1(self):
        tela_imovel1 = self.telas["tela_imovel1"]
        for widget in tela_imovel1.winfo_children(): widget.destroy()
        frame_imovel1 = ttk.Frame(tela_imovel1, style="Card.TFrame", padding=30)
        frame_imovel1.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame_imovel1, text="ZenithPlace", style="Subtitle.TLabel", background=self.card_background, foreground=self.primary_color).pack(pady=10)
        ttk.Label(frame_imovel1, text="Um refúgio de luxo no coração da cidade.\nCom 3 quartos espaçosos, 2 banheiros e 120m² de área.\nAvaliação: Excelente. Ideal para sua família.", justify="center", background=self.card_background, font=("Segoe UI", 11)).pack(pady=15, padx=30)
        ttk.Button(frame_imovel1, text="Ver Semanas Disponíveis", style="Primary.TButton", command=lambda: self.mostrar_tela("tela_listar_imovel1")).pack(pady=25)
        ttk.Button(frame_imovel1, text="Voltar para Empreendimentos", style="Info.TButton", command=lambda: self.mostrar_tela("tela_investimento")).pack(pady=10)

    def configurar_tela_imovel2(self):
        tela_imovel2 = self.telas["tela_imovel2"]
        for widget in tela_imovel2.winfo_children(): widget.destroy()
        frame_imovel2 = ttk.Frame(tela_imovel2, style="Card.TFrame", padding=30)
        frame_imovel2.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame_imovel2, text="Topázio Imperial Hotel", style="Subtitle.TLabel", background=self.card_background, foreground=self.primary_color).pack(pady=10)
        ttk.Label(frame_imovel2, text="Invista em uma suíte exclusiva de 40m² com 1 quarto e 1 banheiro.\nLocalização privilegiada na Avenida Beira Mar. Avaliação: Muito Bom.\nPerfeito para investimento hoteleiro com retornos sólidos.", justify="center", background=self.card_background, font=("Segoe UI", 11)).pack(pady=15, padx=30)
        ttk.Button(frame_imovel2, text="Ver Semanas Disponíveis", style="Primary.TButton", command=lambda: self.mostrar_tela("tela_listar_imovel2")).pack(pady=25)
        ttk.Button(frame_imovel2, text="Voltar para Empreendimentos", style="Info.TButton", command=lambda: self.mostrar_tela("tela_investimento")).pack(pady=10)

    def configurar_tela_imovel3(self):
        tela_imovel3 = self.telas["tela_imovel3"]
        for widget in tela_imovel3.winfo_children(): widget.destroy()
        frame_imovel3 = ttk.Frame(tela_imovel3, style="Card.TFrame", padding=30)
        frame_imovel3.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame_imovel3, text="Petra Palace", style="Subtitle.TLabel", background=self.card_background, foreground=self.primary_color).pack(pady=10)
        ttk.Label(frame_imovel3, text="Residência de alto padrão com 4 quartos, 3 banheiros e 180m².\nLocalizada na desejada Rua das Acácias, Morro Azul.\nAvaliação: Ótima Localização. O ápice do conforto e espaço.", justify="center", background=self.card_background, font=("Segoe UI", 11)).pack(pady=15, padx=30)
        ttk.Button(frame_imovel3, text="Ver Semanas Disponíveis", style="Primary.TButton", command=lambda: self.mostrar_tela("tela_listar_imovel3")).pack(pady=25)
        ttk.Button(frame_imovel3, text="Voltar para Empreendimentos", style="Info.TButton", command=lambda: self.mostrar_tela("tela_investimento")).pack(pady=10)

    def configurar_tela_listar(self, tela_name, imovel_id, imovel_title, return_tela_name):
        tela_listar = self.telas[tela_name]
        for widget in tela_listar.winfo_children(): widget.destroy()
        frame_listar = ttk.Frame(tela_listar, style="Content.TFrame", padding=20)
        frame_listar.pack(fill="both", expand=True)
        frame_listar.grid_rowconfigure(1, weight=1)
        frame_listar.grid_columnconfigure(0, weight=1)

        ttk.Label(frame_listar, text=f"Semanas Disponíveis - {imovel_title}", style="Subtitle.TLabel", background=self.background_color, foreground=self.dark_text).grid(row=0, column=0, pady=(0, 15), sticky="ew")

        colunas = ('id', 'semana', 'periodo', 'valor')
        tabela = ttk.Treeview(frame_listar, columns=colunas, show='headings', style="Treeview")
        tabela.heading('id', text='ID', anchor='center')
        tabela.heading('semana', text='Semana Nº', anchor='center')
        tabela.heading('periodo', text='Período de Uso', anchor='center')
        tabela.heading('valor', text='Valor da Cota (R$)', anchor='e')

        tabela.column('id', width=60, anchor='center', stretch=False)
        tabela.column('semana', width=100, anchor='center')
        tabela.column('periodo', width=200, anchor='center')
        tabela.column('valor', width=150, anchor='e')

        semanas_disponiveis = get_semanas_disponiveis(imovel_id)
        for semana in semanas_disponiveis:
            tabela.insert('', 'end', values=(semana.id, semana.numero_semana, semana.periodo, f"{semana.valor_cota:,.2f}".replace('.', ',')), iid=str(semana.id))
        tabela.grid(row=1, column=0, sticky="nsew", pady=(0, 15), padx=(0, 5))

        scrollbar = ttk.Scrollbar(frame_listar, orient="vertical", command=tabela.yview, style="Vertical.TScrollbar")
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(0, 15))
        tabela.configure(yscrollcommand=scrollbar.set)

        ttk.Button(frame_listar, text="Comprar Semana Selecionada",
                                command=lambda: self.processar_compra_semana(tabela, imovel_id), style="Primary.TButton").grid(row=2, column=0, pady=(10, 5), sticky="ew")

        ttk.Button(frame_listar, text="Voltar", command=lambda: self.mostrar_tela(return_tela_name), style="Info.TButton").grid(row=3, column=0, pady=5, sticky="ew")


    def configurar_tela_listar_imovel1(self):
        self.configurar_tela_listar("tela_listar_imovel1", 1, "ZenithPlace", "tela_imovel1")

    def configurar_tela_listar_imovel2(self):
        self.configurar_tela_listar("tela_listar_imovel2", 2, "Topázio Imperial Hotel", "tela_imovel2")

    def configurar_tela_listar_imovel3(self):
        self.configurar_tela_listar("tela_listar_imovel3", 3, "Petra Palace", "tela_imovel3")


    def processar_compra_semana(self, tabela, imovel_id):
        if not self.current_user:
            messagebox.showerror("Erro", "Você precisa estar logado para comprar uma semana.")
            return

        selected_item = tabela.selection()
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione uma semana para comprar.")
            return
        semana_id = int(selected_item[0]) 
        selected_item_data = tabela.item(selected_item[0])
        row_values = selected_item_data['values']
        semana_numero = row_values[0] 
        semana_periodo = row_values[1]
        semana_valor = row_values[3].replace(',', '.').replace('R$ ', '')

        confirm = messagebox.askyesno("Confirmar Compra", f"Você deseja comprar a Semana Nº {semana_numero} ({semana_periodo}) por R$ {semana_valor}?")

        if confirm:
            sucesso, mensagem = comprar_semana_db(self.current_user.id, semana_id) 
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                if imovel_id == 1:
                    self.configurar_tela_listar_imovel1()
                elif imovel_id == 2:
                    self.configurar_tela_listar_imovel2()
                elif imovel_id == 3: 
                    self.configurar_tela_listar_imovel3() 
                if self.telas["tela_perfil"].winfo_ismapped():
                    self.atualizar_tela_perfil() 
            else:
                messagebox.showerror("Erro", mensagem)

    def saiba_mais(self):
        messagebox.showinfo("O que é Investimento Fracionado?",
        "Acredita que ter um imóvel de luxo está fora do seu alcance? Pense novamente!\n\n"
        "O investimento fracionado oferece a você a oportunidade de ser proprietário de um pedacinho do paraíso. "
        "São 52 semanas no ano, e sua fatia te dá o direito de uso ou de locação.\n\n"
        "Quer usar sua semana para relaxar? À vontade! Quer rentabilizar? "
        "Alugue sua semana de forma prática e segura, transformando seu investimento em uma fonte de renda.\n\n"
        "É a porta de entrada para um mercado exclusivo, com a flexibilidade e a rentabilidade que você sempre buscou.")

if __name__ == "__main__":
    inicializar_dados_imoveis()
    root = tk.Tk()
    app = Sistemainvestimento(root)
    root.mainloop()