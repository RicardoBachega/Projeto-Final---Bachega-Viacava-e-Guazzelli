import armazenamento as amz
import email

base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"
base_dir =  r"C:\Users\RICARDO\Documents\GitHub\Projeto-Final---Bachega-Viacava-e-Guazzelli"

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BBQ(ttk.Frame):
    def __init__(self):
        #janela inicial
        self.window = Tk()
        self.window.title("           BBQ")
        self.window.geometry("360x301+100+100")
        
        self.mainframe = ttk.Frame(self.window)
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
        amz.armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
        self.mostrar_frame(PaginaRelatorio)

    def botao_novo_churrasco(self, cont):
        self.pergunta_se_apaga()
        if self.yesorno == True:
            dicionario_convidados, dicionario_comidas, dicionario_bebidas = amz.novo_churrasco(base_dir)
            self.frames[PaginaCarnes].zerar_checkbuttons()
            self.mostrar_frame(PaginaMyBBQ)           
    
    def pergunta_se_apaga(self):
        self.yesorno = messagebox.askyesno("", "Se você continuar, todos os dados serão apagados. \n Tem certeza de que deseja continuar?")

    def enviar_email(self):
        envia_email(dicionario_convidados + dicionario_bebidas + dicionario_comidas, "ricardo.n.b@hotmail.com")

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
        
#        image = PhotoImage(file='bg1.gif')
#        image1 = ImageTk.PhotoImage(image)
        
        label = ttk.Label(self, text='')
        label.grid(row=0, column=0, sticky="nsew")

        nbbqbutton = ttk.Button(self, text='GERENCIAR CHURRASCO',
                               command=lambda: controller.botao_gerenciar_churrasco(self))

        nbbqbutton.grid(column=2, row=2, sticky=("nsew"))
        
        ebbqbutton = ttk.Button(self, text='NOVO CHURRASCO',
                               command=lambda: controller.botao_novo_churrasco(self))
        ebbqbutton.grid(column=2, row=1, sticky=("nsew"))
        
class PaginaMyBBQ(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(4, minsize=50)
        self.rowconfigure(5, minsize=50)
        self.rowconfigure(6, minsize=50)
        self.columnconfigure(0, minsize=50)
        self.columnconfigure(1, minsize=70)
        self.columnconfigure(2, minsize=50)
        self.columnconfigure(3, minsize=100)
        self.columnconfigure(4, minsize=50)
        self.columnconfigure(5, minsize=50)
        
#        label = ttk.Label(self, text="Meu Churrasco")
#        label.grid(row=0, column=2, sticky="nsew")
        
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

        relatórioButton = ttk.Button(self, text='RELATÓRIO',
                               command=lambda: controller.mostrar_pagina_relatorio(PaginaRelatorio))
        relatórioButton.grid(column=2, row=4, sticky=("nsew"))          
        
        saveexitButton = ttk.Button(self, text='SALVAR E FECHAR',
                               command=lambda: controller.salvar_e_fechar(base_dir))
        saveexitButton.grid(column=2, row=5, sticky=("nsew"))
    
        #botao que volta a pagina inicial
        PIbutton = ttk.Button(self, text='menu inicial',
                               command=lambda: controller.mostrar_frame(PaginaInicial))
        PIbutton.grid(column=2, row=6, sticky=("nsew"))     
    
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
        label = ttk.Label(self, text="Selecione as carnes que \n você deseja em seu churrasco")
        label.grid(row=0, column=1, sticky="nsew")
                
        preçoc = ttk.Label(self, text = 'Preço')        
        preçoc.grid(row=1, column=3, sticky = 'nsew')
        
        self.varc1 = IntVar()
        carne1 = ttk.Label(self, text="Picanha")
        carne1.grid(row=3, column=1, sticky="nsew")
        checkc1 = ttk.Checkbutton(self, variable=self.varc1)
        checkc1.grid(row=3, column=2,sticky="nsew")
        
        self.varc2 = IntVar()                
        carne2 = ttk.Label(self, text="Fraldinha")
        carne2.grid(row=4, column=1, sticky="nsew")
        checkc2 = ttk.Checkbutton(self, variable=self.varc2)
        checkc2.grid(row=4, column=2,sticky="nsew")        
        
        self.varc3 = IntVar()
        carne3 = ttk.Label(self, text="Maminha")
        carne3.grid(row=5, column=1, sticky="nsew")
        checkc3 = ttk.Checkbutton(self, variable=self.varc3)
        checkc3.grid(row=5, column=2,sticky="nsew")        
        
        self.varc4 = IntVar()
        carne4 = ttk.Label(self, text="Contra-filé")
        carne4.grid(row=6, column=1, sticky="nsew")
        checkc4 = ttk.Checkbutton(self,variable=self.varc4)
        checkc4.grid(row=6, column=2,sticky="nsew")
        
        self.varc5 = IntVar()
        carne5 = ttk.Label(self, text="Linguiça")
        carne5.grid(row=7, column=1, sticky="nsew")
        checkc5 = ttk.Checkbutton(self, variable=self.varc5)
        checkc5.grid(row=7, column=2,sticky="nsew")
        
        self.varc6 = IntVar()                                
        carne6 = ttk.Label(self, text="Coração de frango")
        carne6.grid(row=8, column=1, sticky="nsew")
        checkc6 = ttk.Checkbutton(self, variable=self.varc6)
        checkc6.grid(row=8, column=2,sticky="nsew")
        
        VoltarButton = ttk.Button(self, text='VOLTAR',
                               command=lambda: controller.mostrar_frame(PaginaMyBBQ))
        VoltarButton.grid(column=3, row=100, sticky=("nsew"))
        
    def zerar_checkbuttons(self):
        self.varc1.set(0)
        self.varc2.set(0)
        self.varc3.set(0)
        self.varc4.set(0)
        self.varc5.set(0)
        self.varc6.set(0)
        
        
class PaginaBebidas(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Selecione as bebidas que \n você deseja em seu churrasco")
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
        
        self.varbn1 = IntVar()
        bebidab1 = ttk.Label(self, text="Coca-Cola")
        bebidab1.grid(row=11, column=2, sticky="nsew")
        checkbb1 = ttk.Checkbutton(self, variable=self.varbn1)
        checkbb1.grid(row=11, column=3,sticky="nsew")
        
        self.varbn2 = IntVar()
        bebidab2 = ttk.Label(self, text="Guaraná Antártica")
        bebidab2.grid(row=12, column=2, sticky="nsew")
        checkbb2 = ttk.Checkbutton(self, variable=self.varbn2)
        checkbb2.grid(row=12, column=3,sticky="nsew")
        
        self.varbn3 = IntVar()
        bebidab3 = ttk.Label(self, text="Água")
        bebidab3.grid(row=13, column=2, sticky="nsew")
        checkbb3 = ttk.Checkbutton(self, variable=self.varbn3)
        checkbb3.grid(row=13, column=3,sticky="nsew")
        
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