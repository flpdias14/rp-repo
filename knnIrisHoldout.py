#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from math import sqrt




# Método para carregar um arquivo
def loadFile(arquivo, lim):
    # abre o arquivo
    f = open(arquivo)
    # le as linhas do arquivo
    linhas = f.readlines()
    lista = []
    returnList = []
    try:
        for linha in linhas:
            # separa e faz o cast nos valores
            lista = linha.split(",")
            lista[0] = float(lista[0])
            lista[1] = float(lista[1])
            lista[2] = float(lista[2])
            lista[3] = float(lista[3])
            lista[4] = lista[4].replace('\n', '')
            returnList.append(lista)
            lista = []
    except:
        # print '--- fim da leitura do arquivo ' + file + " .---"
        pass
    return returnList

# Método que calcula a distancia euclidiana entre os indivíduos
def calcDistEuclides(individuo1, individuo2):
    y = 2
    soma = pow(individuo1[0] - individuo2[0], y) + pow(individuo1[1] - individuo2[1], y) + pow(individuo1[2] - individuo2[2], y) + pow(individuo1[3] - individuo2[3], y)
    return sqrt(soma)

# Método para classificar um indivíduo, retorna a classe a que o indivíduo pertence
def classificar(treino, individuo, k=1, peso=False):
    # declaração da lista de distancias
    distancias = []

    # declara a variável de retorno
    classificacao = ""
#     calcula as distancias com base nos casos de treino
    for i in treino:
        dist = []
        dist.append(calcDistEuclides(i, individuo))
        # guarda a classe para não se perder na ordenação
        dist.append(i[4])
        distancias.append(dist)
#     ordena os valores
    distancias.sort(cmp=None, key=None, reverse=False)
#     verifica os valores de k
    if k == 1:
        classificacao = distancias[0][1]
    else:
        if peso:
            # Declara listas com labels para contagem de cada classe
            setosa = [0.0, 'Iris-setosa']
            versicolor = [0.0,'Iris-versicolor']
            virginica = [0.0,'Iris-virginica']

            # percorre os k vizinhos
            for i in range(k):

                # verifica se pertence a classe setosa
                if setosa[1] == distancias[i][1]:
    #               incrementa o contador de setosa
                    if  distancias[i][0] != 0:
                        setosa[0] +=1/distancias[i][0]
                    else:
                        setosa[0] += 1000
                # verifica se pertence a classe versicolor
                elif versicolor[1] == distancias[i][1]:
                    # incrementa o contador de versicolor
                    if distancias[i][0] != 0:
                        versicolor[0] +=1/ distancias[i][0]
                    else:
                        versicolor[0] +=1000
    #                 verifica e incremena , caso virginica
                elif virginica[1] == distancias[i][1]:
                    if distancias[i][0] != 0:
                        virginica[0] +=1/distancias[i][0]
                    else:
                        virginica[0] += 1000

            # rank para ordenar as classes
            rank = []
            rank.append(setosa)
            rank.append(versicolor)
            rank.append(virginica)
            # ordena do menor para o maior
            rank.sort(cmp=None, key=None, reverse=False)

            # print rank # pega o maior valor
            classificacao = rank[-1][1]
        else:
            # Declara listas com labels para contagem de cada classe
            setosa = [0.0, 'Iris-setosa']
            versicolor = [0.0,'Iris-versicolor']
            virginica = [0.0,'Iris-virginica']

            # percorre os k vizinhos
            for i in range(k):

                # verifica se pertence a classe setosa
                if setosa[1] == distancias[i][1]:
    #               incrementa o contador de setosa
                    setosa[0] +=1
                # verifica se pertence a classe versicolor
                elif versicolor[1] == distancias[i][1]:
                    # incrementa o contador de versicolor
                    versicolor[0] +=1
    #                 verifica e incremena , caso virginica
                elif virginica[1] == distancias[i][1]:
                    virginica[0] +=1

            # rank para ordenar as classes
            rank = []
            rank.append(setosa)
            rank.append(versicolor)
            rank.append(virginica)
            # ordena do menor para o maior
            rank.sort(cmp=None, key=None, reverse=False)
            # pega o maior valor
            classificacao = rank[-1][1]

    return classificacao


# Método que gera a matriz de confusão
def matrizConfusao(listaClassificada, listaClasses):
    # declaração da matriz
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in listaClassificada:
#         verifica se a classificação foi correta
        if i[4] == i[5]:
#             recupera o indice e adiciona na diagonal
            j = listaClasses.index(i[4])
            matriz[j][j] += 1
        else:
            # pega o indice da linha
            l = listaClasses.index(i[4])
            # pega o indice da coluna
            c = listaClasses.index(i[5])
            matriz[l][c] += 1
    return matriz
# carrega o arquivo de treino e classificação
# listaTreino = loadFile('iris-treino.txt', ',')
# listaClassificar = loadFile('iris-teste.txt', ',')

listaDados = loadFile('iris2.txt', ',')

listaVersicolor = []
listaSetosa = []
listaVirginica = []
listaTreino = []
listaClassificar = []
for a in listaDados:
    if(a[4] == 'Iris-versicolor'):
        listaVersicolor.append(a)
    elif(a[4] == 'Iris-setosa'):
        listaSetosa.append(a)
    else :
        listaVirginica.append(a)
print "lista setosa: "+str(len(listaSetosa))
print "lista virginica: "+str(len(listaVirginica))
print "lista versicolor: "+str(len(listaVersicolor))
listaTreinos = []
listaTestes = []
numVirginica = []
numVersicolor = []
numSetosa = []
numSorteados = []

def sorteiaListaNumeros():
    lista = []
    num = 0
    for i in range(25):
        control = True
        while(control):
            num = randint(0, 49)
            if(lista.count(num) == 0):
                lista.append(num)
                control = False
    return lista


for i in range(100):

    numSorteados = sorteiaListaNumeros()
    for i in numSorteados:
        listaTreino.append(listaSetosa[i])
        listaTreino.append(listaVirginica[i])
        listaTreino.append(listaVersicolor[i])
    for i in range(50):
        if numSorteados.count(i) == 0:
            listaClassificar.append(listaSetosa[i])
            listaClassificar.append(listaVirginica[i])
            listaClassificar.append(listaVersicolor[i])

    listaTreinos.append(listaTreino)
    listaTestes.append(listaClassificar)

    listaTreino = []
    listaClassificar = []

# declaração da lista de individuos classificados
listaClassificada = []
listaClassificados = []
# Classifica os individuos

for i in range(100):
    # print len(listaTestes[i])
    for individuo in listaTestes[i]:

        p = classificar(listaTreinos[i], individuo, k=5, peso=True)
        if len(individuo) == 5:
            individuo.insert(5, p)
        #print p
        listaClassificada.append(individuo)
    listaClassificados.append(listaClassificada)
    listaClassificada = []

# print listaClassificados[i]

# for individuo in listaClassificar:
#     p = classificar(listaTreino, individuo, k=50, peso=False)
#     individuo.insert(5, p)
#     listaClassificada.append(individuo)



def somaLista(lista):
    total = 0
    for num in lista:
        total += num
    return total

def media(lista):
    soma = somaLista(lista)
    media = soma / float(len(lista))
    return media

def variancia(lista):
    media1 = media(lista)
    variancia = 0
    for num in lista:
        variancia += pow((media1 - num), 2.0)
    variancia = variancia / float(len(lista))
    return variancia

def std(variancia):
    return pow(variancia, (0.5))


# contadores de acertos e erros gerais
acertos = 0
erros = 0

classes = []
# contador de acertos das classes
ac1 = 0
ac2 = 0
ac3 = 0
# contador de erros das classes
ec1 = 0
ec2 = 0
ec3 = 0

listaAcertos = []
listaErros = []

for i in range(100):
    for individuo in listaClassificados[i]:
        # print individuo
        if individuo[4] == individuo[5]:
            acertos += 1
        else:
            erros += 1
    listaAcertos.append(acertos)
    listaErros.append(erros)
    acertos = 0
    erros = 0

somaErros = 0
somaAcertos = 0

listaTaxasErro = []
listaTaxasAcerto = []
for i in range(100):
    listaTaxasErro.append((listaErros[i]/float((listaErros[i]+listaAcertos[i]))))

for i in range(100):
    listaTaxasAcerto.append(1-listaTaxasErro[i])


# for i in range(100):
    # print "Acerto teste "+str(i)+": "+str(listaAcertos[i])+ " Erro :"+str(listaErros[i])

print "Media Acertos: " + str(media(listaAcertos))
print "Media Erros: "+str(media(listaErros))
print "Variancia Acertos: "+str(variancia(listaAcertos))
print "Variancia Erros: "+str(variancia(listaErros))
print "Desvio Padrão Acertos: "+ str(std(variancia(listaAcertos)))
print "Desvio Padrão Erros: "+ str(std(variancia(listaErros)))
print "-----------------------------------------------------------"
print "Média taxas Acerto: "+str(media(listaTaxasAcerto)*100)+"%"
print "Média taxas Erro: "+str(media(listaTaxasErro)*100)+"%"
print "Desvio Padrão Taxa Acerto: "+str(std(variancia(listaTaxasAcerto)))
print "Desvio Padrão Taxa Erro: "+str(std(variancia(listaTaxasErro)))


#
# for individuo in listaClassificada:
#     # Separa uma lista com classes
#     if classes.count(individuo[4]) == 0:
#
#         classes.append(individuo[4])
# # Conta erros e acertos de classificação
# for individuo in listaClassificada:
#     # Verifica se a Classificação foi correta
#     if individuo[4] == individuo[5]:
#         # incrementa contador geral de acertos
#         acertos += 1
#         # incrementa contador de acertos da classe
#         if(individuo[5] == classes[0]):
#             ac1 += 1
#         elif (individuo[5] == classes[1]):
#             ac2 += 1
#         else:
#             ac3 += 1
#     else:
#
#         erros += 1
#         if(individuo[5] == classes[0]):
#             ec1 += 1
#         elif individuo[5] == classes[1]:
#             ec2 += 1
#         else:
#             ec3 += 1

# Calcula Erro de Classificação
# err = float(erros) / (erros + acertos)
# # Calcula o erro da classe
# errClasse1 = float(ec1) / (ac1 + ec1)
# errClasse2 = float(ec2) / (ac2 + ec2)
# errClasse3 = float(ec3) / (ac3 + ec3)

# Gera matriz confusão
# matriz = matrizConfusao(listaClassificada, classes)

# print "Acertos : " + str(acertos)
# print "Erros : " + str(erros)
# print "Taxa de Acerto: " + str(1-err)
# print "Taxa de Erro de Classificação : " + str(err)

#
# print "Erro Classe " + classes[0] + " : " + str(errClasse1)
# print "Erro Classe " + classes[1] + " : " + str(errClasse2)
# print "Erro Classe " + classes[2] + " :" + str(errClasse3)

#print "Matriz Confusão:"
#print "| %d %d %d |" % (matriz[0][0], matriz[0][1], matriz[0][2])
#print "| %d %d %d |" % (matriz[1][0], matriz[1][1], matriz[1][2])
#print "| %d %d %d |" % (matriz[2][0], matriz[2][1], matriz[2][2])
