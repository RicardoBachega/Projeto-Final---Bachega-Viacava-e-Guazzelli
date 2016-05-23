# -*- coding: utf-8 -*-

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir =  r"C:\Users\RICARDO\Documents\GitHub\Projeto-Final---Bachega-Viacava-e-Guazzelli"

import armazenamento as amz
import email
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BBQ:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BBQ")
        self.window.geometry("348x300+400+200")
        self.window.iconbitmap(self, default='beef2.ico')
        self.window.resizable(width=False, height=False)
        
        
        #FRAME DA PAGINA INICIAL
        
        self.PaginaInicial = ttk.Frame(self.window)
        self.PaginaInicial.rowconfigure(0, minsize=0)
        self.PaginaInicial.rowconfigure(1, minsize=50)
        self.PaginaInicial.rowconfigure(2, minsize=50)
        self.PaginaInicial.rowconfigure(3, minsize=50)
        self.PaginaInicial.rowconfigure(4, minsize=50)
        self.PaginaInicial.rowconfigure(5, minsize=50)
        self.PaginaInicial.rowconfigure(6, minsize=50)
        self.PaginaInicial.rowconfigure(7, minsize=50)
        self.PaginaInicial.columnconfigure(0, minsize=0)
        self.PaginaInicial.columnconfigure(1, minsize=50)
        self.PaginaInicial.columnconfigure(2, minsize=50)
        self.PaginaInicial.columnconfigure(3, minsize=100)
        self.PaginaInicial.columnconfigure(4, minsize=50)
        self.PaginaInicial.columnconfigure(5, minsize=50)
        self.PaginaInicial.grid(row=0, column=0, sticky="nsew")
        
        self.background_image = tk.PhotoImage(file="bg4.gif")
        self.background = ttk.Label(self.PaginaInicial, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=6, relheight=0.85)
        
        self.ebbqbutton = ttk.Button(self.PaginaInicial)
        self.ebbqbutton.configure(text='GERENCIAR CHURRASCO2', command=self.mostrar_PaginaParticipantes)
        self.ebbqbutton.grid(column=3, row=4, sticky=("nsew"))
        
        self.nbbqbutton = ttk.Button(self.PaginaInicial)
        self.nbbqbutton.configure(text='NOVO CHURRASCO')
        self.nbbqbutton.configure(command=self.mostrar_PaginaMyBBQ)
        self.nbbqbutton.grid(column=3, row=2, sticky=("nsew"))



        #FRAME DA PAGINA MY BBQ

        self.PaginaMyBBQ = tk.Frame(self.window)
        self.PaginaMyBBQ.rowconfigure(1, minsize=50)
        self.PaginaMyBBQ.rowconfigure(2, minsize=50)
        self.PaginaMyBBQ.rowconfigure(3, minsize=50)
        self.PaginaMyBBQ.rowconfigure(4, minsize=50)
        self.PaginaMyBBQ.rowconfigure(5, minsize=50)
        self.PaginaMyBBQ.rowconfigure(6, minsize=50)
        self.PaginaMyBBQ.columnconfigure(0, minsize=50)
        self.PaginaMyBBQ.columnconfigure(1, minsize=70)
        self.PaginaMyBBQ.columnconfigure(2, minsize=50)
        self.PaginaMyBBQ.columnconfigure(3, minsize=100)
        self.PaginaMyBBQ.columnconfigure(4, minsize=50)
        self.PaginaMyBBQ.columnconfigure(5, minsize=50)
        
        #botao dos que acessa os CONVIDADOS
        self.participantesButton = ttk.Button(self.PaginaMyBBQ)
        self.participantesButton.configure(text='CONVIDADOS', command=self.mostrar_PaginaParticipantes)
        self.participantesButton.grid(column=2, row=1, sticky=("nsew"))
        
        #botao da frame CARNES
        self.carnesButton = ttk.Button(self.PaginaMyBBQ)
        self.carnesButton.configure(text='CARNES', command=self.mostrar_PaginaCarnes)
        self.carnesButton.grid(column=2, row=2, sticky=("nsew"))
        
        #botao da frame BEBIDAS
        self.bebidasButton = ttk.Button(self.PaginaMyBBQ)
        self.bebidasButton.configure(text='BEBIDAS', command=self.mostrar_PaginaBebidas)
        self.bebidasButton.grid(column=2, row=3, sticky=("nsew"))        

        #botao da frame LISTA
        self.ListaButton = ttk.Button(self.PaginaMyBBQ)
        self.ListaButton.configure(text='RELATÓRIO', command=self.mostrar_PaginaLista)
        self.ListaButton.grid(column=2, row=4, sticky=("nsew"))          
        
        #botao que salva tudo e fecha o programa
        self.saveexitButton = ttk.Button(self.PaginaMyBBQ)
        self.saveexitButton.configure(text='SALVAR E FECHAR', command=self.salvar_e_fechar)
        self.saveexitButton.grid(column=2, row=5, sticky=("nsew"))
    
        #botao que volta a pagina inicial
        self.PIbutton = ttk.Button(self.PaginaMyBBQ)
        self.PIbutton.configure(text='menu inicial', command=self.mostrar_PaginaInicial)
        self.PIbutton.grid(column=2, row=6, sticky=("nsew"))
        
        
        
        #FRAME DA PAGINA PARTICIPANTES
        
        self.PaginaParticipantes = ttk.Frame(self.window)
        self.PaginaParticipantes.rowconfigure(2, minsize = 50)
        
        self.convidados = ttk.Label(self.PaginaParticipantes, text="CONVIDADOS")
        self.convidados.grid(row=0, column=2, sticky="nsew")
        
        self.VoltarButton = ttk.Button(self.PaginaParticipantes)
        self.VoltarButton.configure(text='VOLTAR', command=self.mostrar_PaginaMyBBQ)
        self.VoltarButton.grid(column=9, row=11, sticky=("nsew"))

        self.homens = ttk.Label(self.PaginaParticipantes)
        self.homens.configure(text='Homens:')
        self.homens.grid(row=2, column=5, sticky='nsew')
        
        self.maisverdeimage = tk.PhotoImage(file="maisverde.gif")
        self.menosvermelhoimage = tk.PhotoImage(file="menosvermelho.gif")
        
        self.maismanButton = ttk.Button(self.PaginaParticipantes)
        self.maismanButton.configure(image=self.maisverdeimage)
        self.maismanButton.grid(row=3, column=7, sticky='nsew')
        
        self.menosmanButton = ttk.Button(self.PaginaParticipantes)
        self.menosmanButton.configure(image=self.menosvermelhoimage)
        self.menosmanButton.grid(row=3, column=3, sticky='nsew')
             
        self.mulheres = ttk.Label(self.PaginaParticipantes)
        self.mulheres.configure(text='Mulheres:')
        self.mulheres.grid(row=5, column=5, sticky='nsew')
        
        self.maiswomanButton = ttk.Button(self.PaginaParticipantes)
        self.maiswomanButton.configure(image=self.maisverdeimage)
        self.maiswomanButton.grid(row=6, column=7, sticky='nsew')
        
        self.menoswomanButton = ttk.Button(self.PaginaParticipantes)
        self.menoswomanButton.configure(image=self.menosvermelhoimage)
        self.menoswomanButton.grid(row=6, column=3, sticky='nsew')
        
        self.criancas = ttk.Label(self.PaginaParticipantes)
        self.criancas.configure(text='Crianças:')
        self.criancas.grid(row=8, column=5, sticky='nsew')
        
        self.maiscriancaButton = ttk.Button(self.PaginaParticipantes)
        self.maiscriancaButton.configure(image=self.maisverdeimage)
        self.maiscriancaButton.grid(row=9, column=7, sticky='nsew')
        
        self.menoscriancaButton = ttk.Button(self.PaginaParticipantes)
        self.menoscriancaButton.configure(image=self.menosvermelhoimage)
        self.menoscriancaButton.grid(row=9, column=3, sticky='nsew')
        
        
        
        #FRAME DA PAGINA DE CARNES
        
        self.PaginaCarnes = ttk.Frame(self.window)
        self.PaginaCarnes.columnconfigure(1, minsize = 50)
        self.PaginaCarnes.columnconfigure(2, minsize = 50)
        self.PaginaCarnes.columnconfigure(3, minsize = 50)
        self.PaginaCarnes.columnconfigure(4, minsize = 50)
        self.PaginaCarnes.columnconfigure(5, minsize = 50)
        
        self.label = ttk.Label(self.PaginaCarnes, text="Selecione as carnes que \n você deseja em seu churrasco")
        self.label.grid(row=0, column=1, sticky="nsew")
        
        self.preçoc = ttk.Label(self.PaginaCarnes, text = 'Preço')        
        self.preçoc.grid(row=1, column=3, sticky = 'nsew')
        
        self.varc1 = tk.IntVar()
        self.carne1 = ttk.Label(self.PaginaCarnes, text="Picanha")
        self.carne1.grid(row=3, column=1, sticky="nsew")
        self.checkc1 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc1)
        self.checkc1.grid(row=3, column=2,sticky="nsew")
        
        self.varc2 = tk.IntVar()                
        self.carne2 = ttk.Label(self.PaginaCarnes, text="Maminha")
        self.carne2.grid(row=4, column=1, sticky="nsew")
        self.checkc2 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc2)
        self.checkc2.grid(row=4, column=2,sticky="nsew")        
        
        self.varc3 = tk.IntVar()
        self.carne3 = ttk.Label(self.PaginaCarnes, text="Fraldinha")
        self.carne3.grid(row=5, column=1, sticky="nsew")
        self.checkc3 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc3)
        self.checkc3.grid(row=5, column=2,sticky="nsew")        
        
        self.varc4 = tk.IntVar()
        self.carne4 = ttk.Label(self.PaginaCarnes, text="Contra-filé")
        self.carne4.grid(row=6, column=1, sticky="nsew")
        self.checkc4 = ttk.Checkbutton(self.PaginaCarnes,variable=self.varc4)
        self.checkc4.grid(row=6, column=2,sticky="nsew")
        
        self.varc5 = tk.IntVar()
        self.carne5 = ttk.Label(self.PaginaCarnes, text="Alcatra")
        self.carne5.grid(row=7, column=1, sticky="nsew")
        self.checkc5 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc5)
        self.checkc5.grid(row=7, column=2,sticky="nsew")
        
        self.varc6 = tk.IntVar()                                
        self.carne6 = ttk.Label(self.PaginaCarnes, text="Coração de frango")
        self.carne6.grid(row=8, column=1, sticky="nsew")
        self.checkc6 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc6)
        self.checkc6.grid(row=8, column=2,sticky="nsew")
        
        self.varc7 = tk.IntVar()                                
        self.carne7 = ttk.Label(self.PaginaCarnes, text="Linguiça")
        self.carne7.grid(row=9, column=1, sticky="nsew")
        self.checkc7 = ttk.Checkbutton(self.PaginaCarnes, variable=self.varc7)
        self.checkc7.grid(row=9, column=2,sticky="nsew")
        
        
        self.VoltarButton = ttk.Button(self.PaginaCarnes)
        self.VoltarButton.configure(text='VOLTAR', command=self.mostrar_PaginaMyBBQ)
        self.VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
        
        
        #FRAME DA PAGINA DE BEBIDAS       
        self.PaginaBebidas = ttk.Frame(self.window)
        
        self.texto_bebidas = ttk.Label(self.PaginaBebidas)
        self.texto_bebidas.configure(text="Selecione as bebidas que \n você deseja em seu churrasco")
        self.texto_bebidas.grid(row=0, column=2, sticky="nsew")
        
        self.bebidas_alcol = ttk.Label(self.PaginaBebidas)
        self.bebidas_alcol.configure(text = 'ALCOÓLICAS')        
        self.bebidas_alcol.grid(row=1, column=2, sticky = 'nsew')
        
        self.preçob = ttk.Label(self.PaginaBebidas)
        self.preçob.configure(text = 'Preço')        
        self.preçob.grid(row=1, column=4, sticky = 'nsew')
        
        self.varb1 = tk.IntVar()
        self.bebida1 = ttk.Label(self.PaginaBebidas, text="Cerveja")
        self.bebida1.grid(row=2, column=2, sticky="nsew")
        self.checkb1 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varb1)
        self.checkb1.grid(row=2, column=3,sticky="nsew")
        
        self.varb2 = tk.IntVar()
        self.bebida2 = ttk.Label(self.PaginaBebidas, text="Vodka")
        self.bebida2.grid(row=3, column=2, sticky="nsew")
        self.checkb2 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varb2)
        self.checkb2.grid(row=3, column=3,sticky="nsew")
        
        self.varb3 = tk.IntVar()
        self.bebida3 = ttk.Label(self.PaginaBebidas, text="Skol Beats")
        self.bebida3.grid(row=4, column=2, sticky="nsew")
        self.checkb3 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varb3)
        self.checkb3.grid(row=4, column=3,sticky="nsew")
        
        self.varb4 = tk.IntVar()
        self.bebida4 = ttk.Label(self.PaginaBebidas, text="")
        self.bebida4.grid(row=5, column=2, sticky="nsew")
        self.checkb4 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varb4)
        self.checkb4.grid(row=5, column=3,sticky="nsew")   
        
        self.varb5 = tk.IntVar()
        self.bebida5 = ttk.Label(self.PaginaBebidas, text="Cachaça")
        self.bebida5.grid(row=5, column=2, sticky="nsew")
        self.checkb5 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varb5)
        self.checkb5.grid(row=5, column=3,sticky="nsew") 
        
        self.espaço = ttk.Label(self.PaginaBebidas, text = '')
        self.espaço.grid(row=9, column=3, sticky='nsew')
        self.bebidas_nalcol = ttk.Label(self.PaginaBebidas, text = 'NÃO ALCOÓLICAS')        
        self.bebidas_nalcol.grid(row=10, column=2, sticky = 'nsew')
        
        self.varbn1 = tk.IntVar()
        self.bebidab1 = ttk.Label(self.PaginaBebidas, text="Coca-Cola")
        self.bebidab1.grid(row=11, column=2, sticky="nsew")
        self.checkbb1 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varbn1)
        self.checkbb1.grid(row=11, column=3,sticky="nsew")
        
        self.varbn2 = tk.IntVar()
        self.bebidab2 = ttk.Label(self.PaginaBebidas, text="Guaraná Antártica")
        self.bebidab2.grid(row=12, column=2, sticky="nsew")
        self.checkbb2 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varbn2)
        self.checkbb2.grid(row=12, column=3,sticky="nsew")
        
        self.varbn3 = tk.IntVar()
        self.bebidab3 = ttk.Label(self.PaginaBebidas, text="Água")
        self.bebidab3.grid(row=13, column=2, sticky="nsew")
        self.checkbb3 = ttk.Checkbutton(self.PaginaBebidas, variable=self.varbn3)
        self.checkbb3.grid(row=13, column=3,sticky="nsew")
        
        self.VoltarButton = ttk.Button(self.PaginaBebidas)
        self.VoltarButton.configure(text='VOLTAR', command=self.mostrar_PaginaMyBBQ)
        self.VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
        
        
        #FRAME DA PAGINA LISTA
        self.PaginaLista = ttk.Frame(self.window)
        
        
        
        self.VoltarButton = ttk.Button(self.PaginaLista)
        self.VoltarButton.configure(text='VOLTAR', command=self.mostrar_PaginaMyBBQ)
        self.VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
        
        
        
        
        
        
        


    def mostrar_PaginaInicial(self):
        self.PaginaInicial.tkraise()         
        
    def mostrar_PaginaMyBBQ(self):
        self.PaginaMyBBQ.tkraise() 
        
    def mostrar_PaginaParticipantes(self):
        self.PaginaParticipantes.tkraise() 
        
    def mostrar_PaginaCarnes(self):
        self.PaginaCarnes.tkraise() 

    def mostrar_PaginaBebidas(self):
        self.PaginaBebidas.tkraise() 
        
    def mostrar_PaginaLista(self):
        self.PaginaLista.tkraise() 
         
    def iniciar(self):
        self.window.mainloop()
     
    def botao_gerenciar_churrasco(self):
       # dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.mostrar_PaginaMyBBQ()   
        
    def zerar_checkbuttons_carnes(self):
        self.varc1.set(0)
        self.varc2.set(0)
        self.varc3.set(0)
        self.varc4.set(0)
        self.varc5.set(0)
        self.varc6.set(0)
        self.varc7.set(0)    
    
    def botao_novo_churrasco(self):
        self.pergunta_se_apaga()
        if self.yesorno == True:
          #  dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.novo_churrasco(base_dir)
            self.PaginaCarnes.zerar_checkbuttons_carnes
            self.mostrar_PaginaMyBBQ
            
    def salvar_e_fechar(self):
       # dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        #amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.window.destroy()
        
    def add_button_homem(self):
        #dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.listbox_convidados.insert(END, self.namevar.get())
        #dicionario_convidados[self.namevar.get()] = 2
        #amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.name_entry.delete(0, 'end')
        
    def add_button_mulher(self):
        #dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        #self.listbox_convidados.insert(END, self.namevar.get())
        #dicionario_convidados[self.namevar.get()] = 1
        #amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.name_entry.delete(0, 'end')
        
    def remover_button(self):
        #dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        #del dicionario_convidados[self.listbox_convidados.delete(ANCHOR)]
        self.listbox_convidados.delete(self.ANCHOR)
    
    def pergunta_se_apaga(self):
        self.yesorno = messagebox.askyesno("Novo Churrasco", "Se você continuar, todos os dados serão apagados. \n Tem certeza de que deseja continuar?")

#    def enviar_email(self):
#        envia_email(dicionario_convidados + dicionario_bebidas + dicionario_comidas, "ricardo.n.b@hotmail.com")

app = BBQ()
app.iniciar()