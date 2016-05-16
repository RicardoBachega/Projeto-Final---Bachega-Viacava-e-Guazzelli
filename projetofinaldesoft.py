import armazenamento as amz
import email

base_dir =  r"C:\Users\B155 FIRE V3\Desktop\Escola\2016\Design de Software\Projeto Final"

from tkinter import *
from tkinter import ttk

class BBQ(ttk.Frame):
    def __init__(self):
        #janela inicial
        self.window = Tk()
        self.window.title("           BBQ")
        self.window.geometry("250x350+100+100")
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
        
        for F in (PaginaInicial, PaginaMyBBQ, PaginaParticipantes, PaginaCarnes, PaginaBebidas):
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
        amz.novo_churrasco(base_dir)
        self.mostrar_frame(PaginaMyBBQ)

class PaginaInicial(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="")
        label.grid(row=0, column=2, sticky="nsew")

        nbbqbutton = ttk.Button(self, text='GERENCIAR CHURRASCO', style = 'NuclearReactor.TButton',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))

        nbbqbutton.grid(column=2, row=1, sticky=("nsew"))
        
        ebbqbutton = ttk.Button(self, text='NOVO CHURRASCO',
                               command=lambda: controller.botao_novo_churrasco(self))
        ebbqbutton.grid(column=2, row=2, sticky=("nsew"))
        
    def botao_gerenciar_apertado(self, controller):
        controller.mostrar_frame(PaginaMyBBQ)
        amz.leitura()
        
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
        PIbutton.grid(column=2, row=5, sticky=("nsew"))                  
        
        saveexitButton = ttk.Button(self, text='SALVAR E FECHAR')
                               #command=lambda: controller.mostrar_frame(PaginaParticipantes))
        saveexitButton.grid(column=2, row=4, sticky=("nsew"))

class PaginaParticipantes(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="CONVIDADOS")
        label.grid(row=0, column=1, sticky="nsew")
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=2, row=100, sticky=("nsew"))

        AddButton = ttk.Button(self, text='Adicionar Convidado')
        AddButton.grid(column=2, row=1, sticky=("nsew"))
        
        #self.namevar = StringVar()
        name = ttk.Entry(self)
        #self.namevar.set(name)
        name.grid(column=1, row=1, sticky=("nsew"))  

        listbox_convidados = Listbox(self)
        listbox_convidados.grid(row=2, column=1, sticky=('nsew'))

        s = ttk.Scrollbar(listbox_convidados, orient=VERTICAL, command=listbox_convidados.yview)
        listbox_convidados.configure(yscrollcommand=s.set)
                

class PaginaCarnes(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(2, minsize = 50)
        self.columnconfigure(3, minsize = 50)
        self.columnconfigure(4, minsize = 50)
        self.columnconfigure(5, minsize = 50)
        label = ttk.Label(self, text="Carnes")
        label.grid(row=0, column=2, sticky="nsew")
                
       #SCROLLBAR
        #s = ttk.Scrollbar(self, orient=VERTICAL, command=listbox.yview)
        #listbox.configure(yscrollcommand=s.set)
                
        preçoc = ttk.Label(self, text = 'Preço')        
        preçoc.grid(row=0, column=4, sticky = 'nsew')
        
        self.varc9 = IntVar()
        carne9 = ttk.Label(self, text="Acém")
        carne9.grid(row=1, column=2, sticky="nsew")
        checkc9 = ttk.Checkbutton(self, variable=self.varc9)
        checkc9.grid(row=1, column=3,sticky="nsew")
        preçoc9 = ttk.Entry(self)
        preçoc9.grid(column=4, row=1, sticky=("nsew")) 
        
        self.varc6 = IntVar()
        #self.varc6.set(0)
        carne6 = ttk.Label(self, text="Alcatra")
        carne6.grid(row=2, column=2, sticky="nsew")
        checkc6 = ttk.Checkbutton(self, variable=self.varc6)
        checkc6.grid(row=2, column=3,sticky="nsew")
        
        self.varc12 = IntVar()
        #self.varc12.set(0)                
        carne12 = ttk.Label(self, text="Contra-Filé")
        carne12.grid(row=3, column=2, sticky="nsew")
        checkc12 = ttk.Checkbutton(self, variable=self.varc12)
        checkc12.grid(row=3, column=3,sticky="nsew")        
        
        self.varc11 = IntVar()
        #self.varc11.set(0)
        carne11 = ttk.Label(self, text="Coxão Duro")
        carne11.grid(row=4, column=2, sticky="nsew")
        checkc11 = ttk.Checkbutton(self, variable=self.varc11)
        checkc11.grid(row=4, column=3,sticky="nsew")        
        
        self.varc8 = IntVar()
        #self.varc8.set(0)
        carne8 = ttk.Label(self, text="Coxão Mole")
        carne8.grid(row=5, column=2, sticky="nsew")
        checkc8 = ttk.Checkbutton(self,variable=self.varc8)
        checkc8.grid(row=5, column=3,sticky="nsew")
        
        self.varc5 = IntVar()
        #self.varc5.set(0)
        carne5 = ttk.Label(self, text="Cupim")
        carne5.grid(row=6, column=2, sticky="nsew")
        checkc5 = ttk.Checkbutton(self, variable=self.varc5)
        checkc5.grid(row=6, column=3,sticky="nsew")
        
        self.varc2 = IntVar()
        #self.varc2.set(0)                        
        carne2 = ttk.Label(self, text="Filé Mignon")
        carne2.grid(row=7, column=2, sticky="nsew")
        checkc2 = ttk.Checkbutton(self, variable=self.varc2)
        checkc2.grid(row=7, column=3,sticky="nsew")
        
        self.varc4 = IntVar()
        #self.varc4.set(0)
        carne4 = ttk.Label(self, text="Fraldinha")
        carne4.grid(row=8, column=2, sticky="nsew")
        checkc4 = ttk.Checkbutton(self, variable=self.varc4)
        checkc4.grid(row=8, column=3,sticky="nsew")
        
        self.varc1 = IntVar()
        #self.varc1.set(0)
        carne1 = ttk.Label(self, text="Maminha")
        carne1.grid(row=9, column=2, sticky="nsew")
        checkc1 = ttk.Checkbutton(self, variable=self.varc1)
        checkc1.grid(row=9, column=3,sticky="nsew")
        
        self.varc7 = IntVar()
        #self.varc7.set(0)        
        carne7 = ttk.Label(self, text="Patinho")
        carne7.grid(row=10, column=2, sticky="nsew")
        checkc7 = ttk.Checkbutton(self, variable=self.varc7)
        checkc7.grid(row=10, column=3,sticky="nsew")        
        
        self.varc3 = IntVar()
        #self.varc3.set(0)
        carne3 = ttk.Label(self, text="Picanha")
        carne3.grid(row=11, column=2, sticky="nsew")
        checkc3 = ttk.Checkbutton(self, variable=self.varc3)
        checkc3.grid(row=11, column=3,sticky="nsew")
        
        self.varc10 = IntVar()
        #self.varc10.set(0)
        carne10 = ttk.Label(self, text="maminha")
        carne10.grid(row=12, column=2, sticky="nsew")
        checkc10 = ttk.Checkbutton(self, variable=self.varc10)
        checkc10.grid(row=12, column=3,sticky="nsew")
        
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
        
        bebidas_nalcol = ttk.Label(self, text = 'NÃO ALCOÓLICAS')        
        bebidas_nalcol.grid(row=10, column=2, sticky = 'nsew')
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
        
app = BBQ()
app.iniciar()