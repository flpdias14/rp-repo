#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
def classificar(treino, individuo, k=1):
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
listaTreino = loadFile('iris-treino.txt', ',')
listaClassificar = loadFile('iris-teste.txt', ',')

# declaração da lista de individuos classificados
listaClassificada = []

# Classifica os individuos

for individuo in listaClassificar:
    p = classificar(listaTreino, individuo, k=5)
    individuo.insert(5, p)
    listaClassificada.append(individuo)

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


for individuo in listaClassificada:
    # Separa uma lista com classes
    if classes.count(individuo[4]) == 0:

        classes.append(individuo[4])
# Conta erros e acertos de classificação
for individuo in listaClassificada:
    # Verifica se a Classificação foi correta
    if individuo[4] == individuo[5]:
        # incrementa contador geral de acertos
        acertos += 1
        # incrementa contador de acertos da classe
        if(individuo[5] == classes[0]):
            ac1 += 1
        elif (individuo[5] == classes[1]):
            ac2 += 1
        else:
            ac3 += 1
    else:

        erros += 1
        if(individuo[5] == classes[0]):
            ec1 += 1
        elif individuo[5] == classes[1]:
            ec2 += 1
        else:
            ec3 += 1

# Calcula Erro de Classificação
err = float(erros) / (erros + acertos)
# Calcula o erro da classe
errClasse1 = float(ec1) / (ac1 + ec1)
errClasse2 = float(ec2) / (ac2 + ec2)
#errClasse3 = float(ec3) / (ac3 + ec3)

# Gera matriz confusão
matriz = matrizConfusao(listaClassificada, classes)

print "Acertos : " + str(acertos)
print "Erros : " + str(erros)
print "Erro de Classificação : " + str(err)
print "Erro Classe " + classes[0] + " : " + str(errClasse1)
print "Erro Classe " + classes[1] + " : " + str(errClasse2)
#print "Erro Classe " + classes[2] + " :" + str(errClasse3)

print "Matriz Confusão:"
print "| %d %d %d |" % (matriz[0][0], matriz[0][1], matriz[0][2])
print "| %d %d %d |" % (matriz[1][0], matriz[1][1], matriz[1][2])
print "| %d %d %d |" % (matriz[2][0], matriz[2][1], matriz[2][2])
