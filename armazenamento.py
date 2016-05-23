import pickle

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
#base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"


#novo
def armazena_variaveis(lista_variaveis, base_dir):
    filename = base_dir + r"\arquivo_variaveis.dados"
    fileobj = open(filename, 'wb')    
    pickle.dump(lista_variaveis, fileobj)
    fileobj.close()

#novo    
def leitura_variaveis(base_dir):
    filename = base_dir + r"\arquivo_variaveis.dados"
    fileobj = open(filename, 'rb')
    variaveis = pickle.load(fileobj)
    return variaveis

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
    dicionario_bebidas = {"Vodka" : 0, "Tequila" : 0, "Whisky" : 0, "Cerveja": 0, "Refrigerante": 0}
    lista_comidas = []
    lista_bebidas = []
    
    armazena(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas

def novo_churrasco(base_dir):
    dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas = leitura(base_dir)
    zera_dicionarios(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir)
    
    return dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas
    
def calcula_quantidades(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, homens, mulheres, crianças, base_dir):
    dicionario_comidas = {"Picanha" : 0, "Maminha" : 0, "Fraldinha" : 0, "Contra-filé" : 0, "Alcatra": 0, "Coração de frango": 0, "Linguiça": 0}
    dicionario_bebidas = {"Vodka" : 0, "Tequila" : 0, "Whisky" : 0, "Cerveja": 0, "Refrigerante": 0}
    if "Picanha" in lista_comidas:
        dicionario_comidas["Picanha"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Maminha" in lista_comidas:
        dicionario_comidas["Maminha"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Fraldinha" in lista_comidas:
        dicionario_comidas["Fraldinha"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Contra-filé" in lista_comidas:
        dicionario_comidas["Contra-filé"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Alcatra" in lista_comidas:
        dicionario_comidas["Alcatra"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Coração de frango" in lista_comidas:
        dicionario_comidas["Coração de frango"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Linguiça" in lista_comidas:
        dicionario_comidas["Linguiça"] += (((homens * 450) + (mulheres * 350) + (crianças * 250))/len(lista_comidas))
    if "Vodka" in lista_bebidas:
        dicionario_bebidas["Vodka"] += (((homens * 300) + (mulheres * 150) + (crianças * 0))/len(lista_bebidas))
    if "Whisky" in lista_bebidas:
        dicionario_bebidas["Whisky"] += (((homens * 300) + (mulheres * 150) + (crianças * 0))/len(lista_bebidas))
    if "Tequila" in lista_bebidas:
        dicionario_bebidas["Tequila"] += (((homens * 300) + (mulheres * 150) + (crianças * 0))/len(lista_bebidas))
    if "Cerveja" in lista_bebidas:
        dicionario_bebidas["Cerveja"] += (((homens * 2000) + (mulheres * 1000) + (crianças * 0))/len(lista_bebidas))
    if "Refrigerante" in lista_bebidas:
        dicionario_bebidas["Refrigerante"] += (((homens * 1000) + (mulheres * 500) + (crianças * 500))/len(lista_bebidas))
    return dicionario_comidas, dicionario_bebidas
    
# homens, mulheres, crianças, picanha, maminha, fraldinha, contra-filé, alcatra, coracao, linguica, whisky, vodka, tequila, cerveja, refrigerante
# lista_variaveis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]