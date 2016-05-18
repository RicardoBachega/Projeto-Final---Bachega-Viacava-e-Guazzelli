import armazenamento as amz
import email

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"

from tkinter import *
from tkinter import ttk


class BBQ(ttk.Frame):
    def __init__(self):
        #janela inicial
        self.window = Tk()
        self.window.title("           BBQ")
        self.window.geometry("400x350+100+100")
        self.window.rowconfigure(0, minsize=50)
        self.window.rowconfigure(1, minsize=50)
        self.window.rowconfigure(2, minsize=50)
        self.window.rowconfigure(3, minsize=50)
        self.window.rowconfigure(4, minsize=50)
        self.window.rowconfigure(5, minsize=50)
        self.window.rowconfigure(6, minsize=50)
        self.window.rowconfigure(7, minsize=50)
        self.window.columnconfigure(0, minsize=50)
        self.window.columnconfigure(1, minsize=50)
        self.window.columnconfigure(2, minsize=50)
        self.window.columnconfigure(3, minsize=50)
        self.window.columnconfigure(4, minsize=50)
        
        self.mainframe = ttk.Frame(self.window, padding = "3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=("nsew"))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        
        self.window.iconbitmap(self, default='beef2.ico')
       
        self.frames = {}
        
        for F in (PaginaInicial, PaginaMyBBQ, PaginaParticipantes, PaginaCarnes, PaginaBebidas, PaginaRelatorio):

            frame = F(self.mainframe, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.mostrar_frame(PaginaInicial)            
    
    def mostrar_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()    
    
    def iniciar(self):
        self.window.mainloop()   
    
    def botao_novo_churrasco(self, cont):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.novo_churrasco(base_dir)
        self.mostrar_frame(PaginaMyBBQ)
    
    def botao_gerenciar_churrasco(self, cont):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.mostrar_frame(PaginaMyBBQ)

    def salvar_e_fechar(self, base_dir):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.window.destroy()
        
    def mostrar_pagina_relatorio(self, cont):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.calcula_quantidades(dicionario_convidados, dicionario_bebidas, dicionario_comidas, base_dir)
        armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.mostrar_frame(PaginaRelatorio)


class PaginaInicial(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.rowconfigure(0, minsize=50)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(4, minsize=50)
        self.rowconfigure(5, minsize=50)
        self.rowconfigure(6, minsize=50)
        self.rowconfigure(7, minsize=50)
        self.columnconfigure(0, minsize=50)
        self.columnconfigure(1, minsize=50)
        self.columnconfigure(2, minsize=50)
        self.columnconfigure(3, minsize=100)
        self.columnconfigure(4, minsize=50)
        self.columnconfigure(5, minsize=50)
        
        label = ttk.Label(self, text="")
        label.grid(row=3, column=3, sticky="nsew")

        nbbqbutton = ttk.Button(self, text='GERENCIAR CHURRASCO',
                               command=lambda: controller.botao_gerenciar_churrasco(self))

        nbbqbutton.grid(column=2, row=1, sticky=("nsew"))
        
        ebbqbutton = ttk.Button(self, text='NOVO CHURRASCO',
                               command=lambda: controller.botao_novo_churrasco(self))
        ebbqbutton.grid(column=2, row=2, sticky=("nsew"))
        
class PaginaMyBBQ(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Meu Churrasco")
        label.grid(row=0, column=2, sticky="nsew")
        
        #botao dos que acessa os CONVIDADOS
        participantesButton = ttk.Button(self, text='CONVIDADOS',
                               command=lambda: controller.mostrar_frame(PaginaParticipantes))
        participantesButton.grid(column=2, row=1, sticky=("nsew"))
        
        #botao da lista de CARNES
        carnesButton = ttk.Button(self, text='CARNES',
                               command=lambda: controller.mostrar_frame(PaginaCarnes))
        carnesButton.grid(column=2, row=2, sticky=("nsew"))
        
        #botao da lista de BEBIDAS
        bebidasButton = ttk.Button(self, text='BEBIDAS',
                               command=lambda: controller.mostrar_frame(PaginaBebidas))
        bebidasButton.grid(column=2, row=3, sticky=("nsew")) 

        #botao que volta a pagina inicial
        PIbutton = ttk.Button(self, text='menu inicial',
                               command=lambda: controller.mostrar_frame(PaginaInicial))
        PIbutton.grid(column=2, row=6, sticky=("nsew"))        

        relatórioButton = ttk.Button(self, text='RELATÓRIO',
                               command=lambda: controller.mostrar_pagina_relatorio(PaginaRelatorio))
        relatórioButton.grid(column=2, row=4, sticky=("nsew"))          
        
        saveexitButton = ttk.Button(self, text='SALVAR E FECHAR',
                               command=lambda: controller.salvar_e_fechar(base_dir))
        saveexitButton.grid(column=2, row=5, sticky=("nsew"))
    
    def mostrar_pagina_participantes(self, cont):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.mostrar_frame(PaginaParticipantes)

class PaginaParticipantes(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.rowconfigure(2, minsize = 50)
        label = ttk.Label(self, text="CONVIDADOS")
        label.grid(row=0, column=1, sticky="nsew")
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=2, row=100, sticky=("nsew"))
        
        #self.greenplus = PhotoImage(file='+verde.jpg')
        self.AddMButton = ttk.Button(self, text='Adicionar Homem', command=self.add_button_homem)
        self.AddMButton.grid(column=2, row=1, sticky=("nsew"))
        self.AddWButton = ttk.Button(self, text='Adicionar Mulher', command=self.add_button_mulher)
        self.AddWButton.grid(column=3, row=1, sticky="nsew")
        
        #redX = PhotoImage(file='redX(1).jpg')
        removeButton = ttk.Button(self, text="Remover Convidado", command = self.remover_button)
        removeButton.grid(column=2, row=2, sticky=("new"))
        
        self.namevar = StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.namevar)
        self.name_entry.focus_set()     
        self.name_entry.grid(column=1, row=1, sticky=("nsew"))
        
        self.listbox_convidados = Listbox(self)
        self.listbox_convidados.grid(row=2, column=1, sticky=('nsew'))
                
        #s = ttk.Scrollbar(listbox_convidados, orient=VERTICAL, command=listbox_convidados.yview)
        #listbox_convidados.configure(yscrollcommand=s.set)

    def add_button_homem(self):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.listbox_convidados.insert(END, self.namevar.get())
        dicionario_convidados[self.namevar.get()] = 2
        amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.name_entry.delete(0, 'end')
        
    def add_button_mulher(self):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        self.listbox_convidados.insert(END, self.namevar.get())
        dicionario_convidados[self.namevar.get()] = 1
        amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.name_entry.delete(0, 'end')
        
    def remover_button(self):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        del dicionario_convidados[self.listbox_convidados.delete(ANCHOR)]
        self.listbox_convidados.delete(ANCHOR)

class PaginaCarnes(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(1, minsize = 50)
        self.columnconfigure(2, minsize = 50)
        self.columnconfigure(3, minsize = 50)
        self.columnconfigure(4, minsize = 50)
        self.columnconfigure(5, minsize = 50)
        label = ttk.Label(self, text="Quais carnes você deseja")
        label2 = ttk.Label(self, text="em seu churrasco?")
        label.grid(row=0, column=1, sticky="nsew")
        label2.grid(row=1, column=1, sticky="nsew")
                
       #SCROLLBAR
        #s = ttk.Scrollbar(self, orient=VERTICAL, command=listbox.yview)
        #listbox.configure(yscrollcommand=s.set)
                
        preçoc = ttk.Label(self, text = 'Preço')        
        preçoc.grid(row=0, column=3, sticky = 'nsew')
        
#        self.varc9 = IntVar()
#        carne9 = ttk.Label(self, text="Acém")
#        carne9.grid(row=1, column=1, sticky="nsew")
#        checkc9 = ttk.Checkbutton(self, variable=self.varc9)
#        checkc9.grid(row=1, column=2,sticky="nsew")
#        preçoc9 = ttk.Entry(self)
#        preçoc9.grid(column=3, row=1, sticky=("nsw")) 
        
        self.varc6 = IntVar()
        #self.varc6.set(0)
        carne6 = ttk.Label(self, text="Picanha")
        carne6.grid(row=2, column=1, sticky="nsew")
        checkc6 = ttk.Checkbutton(self, variable=self.varc6)
        checkc6.grid(row=2, column=2,sticky="nsew")
        
        self.varc12 = IntVar()
        #self.varc12.set(0)                
        carne12 = ttk.Label(self, text="Fraldinha")
        carne12.grid(row=3, column=1, sticky="nsew")
        checkc12 = ttk.Checkbutton(self, variable=self.varc12)
        checkc12.grid(row=3, column=2,sticky="nsew")        
        
        self.varc11 = IntVar()
        #self.varc11.set(0)
        carne11 = ttk.Label(self, text="Maminha")
        carne11.grid(row=4, column=1, sticky="nsew")
        checkc11 = ttk.Checkbutton(self, variable=self.varc11)
        checkc11.grid(row=4, column=2,sticky="nsew")        
        
        self.varc8 = IntVar()
        #self.varc8.set(0)
        carne8 = ttk.Label(self, text="Contra-filé")
        carne8.grid(row=5, column=1, sticky="nsew")
        checkc8 = ttk.Checkbutton(self,variable=self.varc8)
        checkc8.grid(row=5, column=2,sticky="nsew")
        
        self.varc5 = IntVar()
        #self.varc5.set(0)
        carne5 = ttk.Label(self, text="Linguiça")
        carne5.grid(row=6, column=1, sticky="nsew")
        checkc5 = ttk.Checkbutton(self, variable=self.varc5)
        checkc5.grid(row=6, column=2,sticky="nsew")
        
        self.varc2 = IntVar()
        #self.varc2.set(0)                        
        carne2 = ttk.Label(self, text="Coração de frango")
        carne2.grid(row=7, column=1, sticky="nsew")
        checkc2 = ttk.Checkbutton(self, variable=self.varc2)
        checkc2.grid(row=7, column=2,sticky="nsew")
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
class PaginaBebidas(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="BEBIDAS")
        label.grid(row=0, column=2, sticky="nsew")
        
        bebidas_alcol = ttk.Label(self, text = 'ALCOÓLICAS')        
        bebidas_alcol.grid(row=1, column=2, sticky = 'nsew')
        
        preçob = ttk.Label(self, text = 'Preço')        
        preçob.grid(row=1, column=4, sticky = 'nsew')
        
        self.varb1 = IntVar()
        bebida1 = ttk.Label(self, text="Cerveja")
        bebida1.grid(row=2, column=2, sticky="nsew")
        checkb1 = ttk.Checkbutton(self, variable=self.varb1)
        checkb1.grid(row=2, column=3,sticky="nsew")
        
        self.varb2 = IntVar()
        bebida2 = ttk.Label(self, text="Vodka")
        bebida2.grid(row=3, column=2, sticky="nsew")
        checkb2 = ttk.Checkbutton(self, variable=self.varb2)
        checkb2.grid(row=3, column=3,sticky="nsew")
        
        self.varb3 = IntVar()
        bebida3 = ttk.Label(self, text="Skol Beats")
        bebida3.grid(row=4, column=2, sticky="nsew")
        checkb3 = ttk.Checkbutton(self, variable=self.varb3)
        checkb3.grid(row=4, column=3,sticky="nsew")
        
        self.varb4 = IntVar()
        bebida4 = ttk.Label(self, text="")
        bebida4.grid(row=5, column=2, sticky="nsew")
        checkb4 = ttk.Checkbutton(self, variable=self.varb4)
        checkb4.grid(row=5, column=3,sticky="nsew")   
        
        self.varb5 = IntVar()
        bebida5 = ttk.Label(self, text="Cachaça")
        bebida5.grid(row=5, column=2, sticky="nsew")
        checkb5 = ttk.Checkbutton(self, variable=self.varb5)
        checkb5.grid(row=5, column=3,sticky="nsew") 
        
        espaço = ttk.Label(self,text = '')
        espaço.grid(row=9, column=3, sticky='nsew')
        bebidas_nalcol = ttk.Label(self, text = 'NÃO ALCOÓLICAS')        
        bebidas_nalcol.grid(row=10, column=2, sticky = 'nsew')
        
        self.varb11 = IntVar()
        bebida11 = ttk.Label(self, text="Coca-Cola")
        bebida11.grid(row=11, column=2, sticky="nsew")
        checkb11 = ttk.Checkbutton(self, variable=self.varb11)
        checkb11.grid(row=11, column=3,sticky="nsew")
        
        self.varb12 = IntVar()
        bebida12 = ttk.Label(self, text="Guaraná Antártica")
        bebida12.grid(row=12, column=2, sticky="nsew")
        checkb12 = ttk.Checkbutton(self, variable=self.varb12)
        checkb12.grid(row=12, column=3,sticky="nsew")
        
        self.varb13 = IntVar()
        bebida13 = ttk.Label(self, text="Água")
        bebida13.grid(row=13, column=2, sticky="nsew")
        checkb13 = ttk.Checkbutton(self, variable=self.varb13)
        checkb13.grid(row=13, column=3,sticky="nsew")
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
class PaginaRelatorio(ttk.Frame):
    
    def __init__(self, parent, controller):
        dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.leitura(base_dir)
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Relatório")
        label.grid(row=0, column=2, sticky="nsew")
        label2 = ttk.Label(self, text=dicionario_convidados)
        label2.grid(row=1, column = 2, sticky="nsew")
        label3 = ttk.Label(self, text=dicionario_comidas)
        label3.grid(row=2, column = 2, sticky="nsew")
        label4 = ttk.Label(self, text=dicionario_bebidas)
        label4.grid(row=3, column=2, sticky="nsew")
    
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
app = BBQ()
app.iniciar()