import pickle

#base_dir =  r"C:\Users\Henrique\Documents\DESOFT\Projeto-Final---Bachega-Viacava-e-Guazzelli"
base_dir = r"C:\Users\B155 FIRE V3\Documents\Projeto-Final---Bachega-Viacava-e-Guazzelli"

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
    
def adiciona_a_lista_comidas(self, variavel, nome, lista_comidas):
    dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas = leitura(base_dir)
    if nome not in lista_comidas:
        if variavel == 1:
            lista_comidas.append(nome)
    elif nome in lista_comidas:
        if variavel == 0:
            lista_comidas.remove(nome)
    armazena(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir)
    return lista_comidas
    
def adiciona_a_lista_bebidas(self, variavel, nome, lista_bebidas):
    dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas = leitura(base_dir)
    if nome not in lista_bebidas:
        if variavel == 1:
            lista_bebidas.append(nome)
    elif nome in lista_bebidas:
        if variavel == 0:
            lista_bebidas.remove(nome)
    armazena(dicionario_comidas, dicionario_bebidas, lista_comidas, lista_bebidas, base_dir)
    return lista_bebidas
    
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