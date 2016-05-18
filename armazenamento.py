import pickle

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"

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
    
    dicionario_comidas = {"Picanha" : 0, "Fraldinha" : 0, "Maminha" : 0, "Alcatra" : 0}
    dicionario_bebidas = {"Vodka" : 0, "Tequila" : 0, "Whisky" : 0}
    dicionario_convidados = {}
    
    armazena(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, dicionario_convidados
    
def novo_churrasco(base_dir):
    dicionario_convidados, dicionario_comidas, dicionario_bebidas = leitura(base_dir)
    zera_dicionarios(dicionario_comidas, dicionario_bebidas, dicionario_convidados, base_dir)
    
    return dicionario_convidados, dicionario_comidas, dicionario_bebidas
    
def calcula_quantidades(dicionario_convidados, dicionario_bebidas, dicionario_comidas, base_dir):
    for i in range(len(dicionario_convidados)):
        if dicionario_convidados[i] == 1:
            for j in range(len(dicionario_comidas)):
                dicionario_comidas[j] += 250/len(dicionario_comidas)
            for j in range(len(dicionario_bebidas)):
                dicionario_bebidas[j] += 250/len(dicionario_bebidas)
        else:
            for j in range(len(dicionario_comidas)):
                dicionario_comidas[j] += 500/len(dicionario_comidas)
            for j in range(len(dicionario_bebidas)):
                dicionario_bebidas[j] += 500/len(dicionario_bebidas)
    return dicionario_convidados, dicionario_comidas, dicionario_comidas