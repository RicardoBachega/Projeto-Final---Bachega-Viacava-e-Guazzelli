import pickle

def armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir):
    
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
    pickle.dump(dicionario_convidados, fileobj)    
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
    
    return convidados, comidas, bebidas
    
def zera_dicionarios(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir):
    
    dicionario_comidas = {}
    dicionario_bebidas = {}
    dicionario_convidados = {}

    armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, dicionario_convidados
    
def novo_churrasco(base_dir):
    dicionario_convidados, dicionario_comidas, dicionario_bebidas = leitura(base_dir)
    zera_dicionarios(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
    armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)

    convidados = dicionario_convidados
    comidas = dicionario_comidas
    bebidas = dicionario_bebidas
    
    return convidados, comidas, bebidas
