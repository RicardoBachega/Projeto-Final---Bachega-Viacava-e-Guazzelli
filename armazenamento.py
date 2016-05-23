import pickle

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"

def armazena(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir):
    
    filename = base_dir + r"\arquivo_comidas.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(dicionario_comidas, fileobj)    
    fileobj.close()
    
    filename = base_dir + r"\arquivo_bebidas.dados"
    fileobj = open(filename, 'wb')
    pickle.dump(dicionario_bebidas, fileobj)    
    fileobj.close()
    
    filename = base_dir + r"\arquivo_comidas_lista.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(lista_comidas, fileobj)    
    fileobj.close()
    
    filename = base_dir + r"\arquivo_bebidas_lista.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(lista_comidas, fileobj)    
    fileobj.close()

def leitura(base_dir):
    
    filename = base_dir + r"\arquivo_comidas.dados"
    fileobj = open(filename, 'rb')
    comidas = pickle.load(fileobj)  
    
    filename = base_dir + r"\arquivo_bebidas.dados"    
    fileobj = open(filename, 'rb')
    bebidas = pickle.load(fileobj)
    
    filename = base_dir + r"\arquivo_comidas_lista.dados"
    fileobj = open(filename, 'rb')
    comidas_lista = pickle.load(fileobj)

    filename = base_dir + r"\arquivo_bebidas_lista.dados"
    fileobj = open(filename, 'rb')
    bebidas_lista = pickle.load(fileobj)
    
    return comidas, bebidas, comidas_lista, bebidas_lista
    
def zera_dicionarios(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir):
    
    dicionario_comidas = {"Picanha" : 0, "Maminha" : 0, "Fraldinha" : 0, "Contra-filé" : 0, "Alcatra": 0, "Coração de frango": 0, "Linguiça": 0}
    dicionario_bebidas = {"Vodka" : 0, "Tequila" : 0, "Whisky" : 0, "Cerveja": 0, "Refrigerante": 0, "Água": 0}
    lista_comidas = []
    lista_bebidas = []
    
    armazena(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas
    
def novo_churrasco(base_dir):
    dicionario_comidas, dicionario_bebidas = leitura(base_dir)
    zera_dicionarios(dicionario_comidas, dicionario_bebidas, base_dir)
    
    return dicionario_comidas, dicionario_bebidas