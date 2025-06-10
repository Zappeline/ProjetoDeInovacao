import tkinter as tk
from models.SistemaTransacao import SistemaTransacao
from models.Semanas import Semanas
from models.Imoveis import Imoveis
from models.Usuarios import Usuarios

ZenithPlace = Imoveis(1, "Casa", "Rua das Flores, 123", 1365000, 5, 3, "100m²", "9.7 - Excelente")
GoldenCoast = Imoveis(2, "Casa", "Avenida do Sol, 456", 1365000, 4, 2, "150m²", "9.5 - Muito Bom")
Semanas = []
SistemaTransacao = (1365.000)


class Sistemainvestimento:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistema de Investimento Fracionado")
        self.root.geometry("600x400")
        self.root.rezizable(True, True)
        
        #container tela
        self.container = tk.frame.Frame(root)
        self.container.pack(fill="both", expand=True) 

        self.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.tela_login = tk.Frame(self.container)
        self.tela_principal = tk.Frame(self.container)
        self.tela_perfil = tk.Frame(self.container)
        self.tela_atualizar_cadastro = tk.Frame(self.container)
        self.tela_investimento = tk.Frame(self.container)
        self.tela_imovel1 = tk.Frame(self.container)
        self.tela_imovel2 = tk.Frame(self.container)
        self.tela_listar_imovel1 = tk.Frame(self.container)
        self.tela_listar_imovel1.grid(row=0, column = 0)
        self.tela_listar_imovel2 = tk.Frame(self.container)
        self.tela_saibamais = tk.Frame(self.container)

        for tela in (self.tela_principal,self.tela_login,self.tela_perfil,self.tela_atualizar_cadastro, 
                    self.tela_investimento,self.tela_imovel1,self.tela_imovel2,self.tela_listar_imovel1,
                    self.tela_listar_imovel2,self.tela_saibamais):
            tela.grid(row = 0, column = 0, sticky="nsew")
            
        
        self.tela_login = tk.Frame()
        self.tela_principal = tk.Frame()
        self.tela_perfil = tk.Frame()
        self.tela_atualizar_cadastro = tk.Frame()
        self.tela_investimento = tk.Frame()
        self.tela_imovel1 = tk.Frame()
        self.tela_imovel2 = tk.Frame()
        self.tela_listar_imovel1 = tk.Frame()
        self.tela_listar_imovel2 = tk.Frame()
        self.tela_saibamais = tk.Frame()
        
        self.mostrar_tela(self.tela_login)
    def mostrar_tela(self,tela):
        tela.tkraise()
    def configurar_tela_login (self):
        frame = tk.Frame(self.tela_login, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
    
        titulo = tk.Label(frame, text="Login", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 30))
        
        tk.Label(form_frame, text="CPF:").grid(row=0, column=0, sticky="e", pady=5)
        self.placa_entry = tk.Entry(form_frame, width=15)
        self.placa_entry.grid(row=0, column=1, sticky="w", pady=5)

        