import tkinter as tk
class Sistemainvestimento:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistema de Investimento Fracionado")
        self.root.geometry("600x400")
        self.root.rezizable(True, True)
        
        #container tela
        self.container = tk.frame.Frame(root)
        self.container.pack(fill="both", expand=True) 


#OLA MUNDOA  