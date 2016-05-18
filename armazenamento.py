import pickle

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"

def armazena(dicionario_comidas, dicionario_bebidas, lista_convidados, lista_quantidades, base_dir):
    
    filename = base_dir + r"\arquivo_comidas.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(dicionario_comidas, fileobj)    
    fileobj.close()
    
    filename = base_dir + r"\arquivo_bebidas.dados"
    fileobj = open(filename, 'wb')
    pickle.dump(dicionario_bebidas, fileobj)    
    fileobj.close()
    
    filename = base_dir + r"\arquivo_convidados.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(lista_convidados, fileobj)    
    fileobj.close()

    filename = base_dir + r"\arquivo_convidados.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(lista_quantidades, fileobj)    
    fileobj.close()
    
def leitura(base_dir):
    
    filename = base_dir + r"\arquivo_convidados.dados"
    fileobj = open(filename, 'rb')
    convidados = pickle.load(fileobj)
    
    filename = base_dir + r"\arquivo_comidas.dados"
    fileobj = open(filename, 'rb')
    comidas = pickle.load(fileobj)  
    
    filename = base_dir + r"\arquivo_bebidas.dados"    
    fileobj = open(filename, 'rb')
    bebidas = pickle.load(fileobj)
    
    filename = base_dir + r"\arquivo_quantidades.dados"    
    fileobj = open(filename, 'rb')
    quantidades = pickle.load(fileobj)

    return convidados, comidas, bebidas, quantidades
    
def zera_dicionarios(dicionario_comidas, dicionario_bebidas, lista_convidados, lista_quantidades, base_dir):
    
    dicionario_comidas = {"Picanha" : 0, "Fraldinha" : 0, "Maminha" : 0, "Alcatra" : 0}
    dicionario_bebidas = {"Vodka" : 0, "Tequila" : 0, "Whisky" : 0}
    lista_convidados = []
    lista_quantidades = []
    
    armazena(dicionario_comidas, dicionario_bebidas, lista_convidados, lista_quantidades, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, lista_convidados, lista_quantidades
    
def novo_churrasco(base_dir):
    dicionario_convidados, dicionario_comidas, dicionario_bebidas, lista_quantidades = leitura(base_dir)
    zera_dicionarios(dicionario_comidas, dicionario_bebidas, dicionario_convidados, lista_quantidades, base_dir)
    
    return dicionario_convidados, dicionario_comidas, dicionario_bebidas, lista_quantidades