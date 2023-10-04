# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:00:58 2020

@author: 1jean
"""

import math

def Créer_Pile():
    '''crée une liste vide, symbolisant une pile vide. Cette fonction ne
    prend aucun argument (type none) et renvoie en sortie une
    liste vide(type list).'''
    return list()
    
def Empiler(liste,element):
    '''ajoute un élément sur le dessus de la pile. Cet élément devient alors le
    premier et son indice est supérieur d'une unité à «l'ex-premier» élément.
    Cette fonction prend en argument la pile(type list), ainsi que 
    l’élément à empiler (type str ou type int ou type float)
    et ne renvoie rien en sortie(type none)'''
    liste.append(element)

def Dépiler(liste):
    '''retire le premier élément de la pile. Cette fonction prend en argument
    une pile(type list) et renvoie en sortie la valeur de cet élément
    (type str ou int ou float), ou un message d’erreur si la pile est vide.'''
    if liste==list():
        return 'La PILE est vide'
    else:
        return liste.pop()

def Pile_Vide(pile):
     '''renvoie TRUE si et seulement si la pile est vide. Primitive importante,
     car il est impossible de dépiler une pile vide. Prend en argument une 
     pile(type list), et renvoie en sortie un booléen.'''
     return pile==[]
    
def Longueur(P):
     '''Prend en argument une pile (type list) et renvoie en sortie 
     un entier(type int) qui est la longueur de cette pile
     return len(P)'''
     
def Premier(P):
    '''prend en argument une pile(type list) et renvoie en sortie la 
    valeur du premier 
    élément de la pile, sans le dépiler. Si la pile est vide, renvoie un
    message d’erreur.'''
    if Pile_Vide(P):
        return "La Pile est vide"
    else:
        sauvegarde=P.pop()
        P.append(sauvegarde)
        return sauvegarde
######################################################
# EXERCICE 01
######################################################
def Deg(P):
    '''Fonction qui prend en argument un polynôme sous forme d’une liste
    (type list) et renvoie en sortie le degré de ce polynôme sous forme d'un 
    entier naturel(type int) s'il est non nul, et le flottant -math.inf 
    (type float) s'il est nul.'''
    while Premier(P)==0:
    #Tant que le dernier élément de la liste est un 0 .
        Dépiler(P)
    #On supprime le dernier élément de la liste qui est 0 .
    if P==[]:
    #Si P est la liste vide : Cela signifie que la liste ne contenait que des 0 
    #et correspondait donc au polynôme nul .
        return -math.inf
    #On retourne le flottant -math.inf qui modélise le degré - l'infini .
    else:
    #Si P n'est pas la liste vide .
        return len(P)-1
    #On retourne len(P)-1 qui est le degré du monôme de plus haut degré .
    #Car le degré du polynôme est le degré de son monôme de plus haut degré .

######################################################
# EXERCICE 02
######################################################
def Afficher(P):
    degrés=[]
    polynôme=[]
    #On crée les listes degrés et polynôme.
    S=''
    #On crée la chaîne de caractère vide S.
    while Premier(P)==0:
        Dépiler(P)
    #On supprime les 0 superflus se situant en fin de liste .
    for i in range(0,len(P)):
    #Pour i allant de 0 à la longueur de la liste -1 .
        Empiler(degrés,'^'+str(i))
    #On ajoute concatène '^' et str(i) et on ajoute cette chaîne de caractères
    #'^i' dans la liste degrés .
    while P.count(0)>0:
    #Tant que le nombre de 0 dans la liste P est strictement supérieur à 0 .
            del(degrés)[P.index(0)]
    #On supprime l'élément de la liste degrés ayant le même indexe que le 0 
    #le plus proche du début de la liste P .
            del(P)[P.index(0)]
    #On retire à P le 0 le plus proche de son début .
    for i in range(0,len(P)):
    #Pour i allant de 0 à (longueur de la liste P)                                                                                                          - 1 .
        if degrés[i]=='^0':
    #Si le degré du i-ème monôme est 0 .
            Empiler(polynôme,str(P[i]))
    #On ajoute 'le coefficient de ce i-ème monopole' à la liste polynôme .
        elif degrés[i]=='^1' and P[i]==1:
    #Si le i-ème élément de P est égal à 1 et que son degré associé est 1 .
            Empiler(polynôme,'X')
    #On ajoute 'X' à la liste polynôme .
        elif P[i]==1:
    #Si le i-ème élément de P est égal à 1.
            Empiler(polynôme,str('X'+degrés[i]))
    #On ajoute la concaténation de 'X' et'^(degré associé à i)' à la liste polynôme.
        elif degrés[i]=='^1':
    #Si le degré du i-ème monôme est 1 .
            Empiler(polynôme,str(P[i])+' X')
    #On ajoute la concaténation de 'X' avec 'le coefficient du i-ème monôme
    #à la liste polynôme' .
        else:
            Empiler(polynôme,str(P[i])+' X'+degrés[i])
    #Dans les autres cas on transforme le coefficient du i-ème monome en chaîne
    #de caractères et on le  concatène avec 'X' et le degré de ce i-ème monome.
    S=S+polynôme[-1]
    #On concatène le dernier terme de la liste polynôme avec la chaîne de 
    #caractère vide S.Ce dernier terme est le monôme de plus haut degré .
    for s in polynôme[len(polynôme)-2::-1]:
    #s parcourt la liste polynôme dont on a retiré le dernier terme et 
    #qui a été inversée .
        if list(s)[0]=='-':
    #Si le premier élément du monôme s est un signe - .
            S=S+' - '+s[1:]
    #On ajoute la concaténation de S ' - ' et s[1:].s[1:] est s privé de son 
    # premier terme d'indexe 0 qui dans ce cas était - .
        else:
            S=S+' + '+s
    #Dans S on ajoute la concaténation de S ' + ' et s 
    print(S)
    #On affiche le résultat dans la console . 

######################################################
# EXERCICE 03
######################################################
def Additionner(P,Q):
    '''Fonction qui prend en argument deux polynômes sous la forme de listes
    (type list)et qui retourne en sortie le polynôme (sous la forme d’une liste)
    ́(type list) égal à la somme des deux polynômes pris en argument.'''
    résultat=[]
    for i in range(max(len(P),len(Q))):
        while len(P)>len(Q):
            Empiler(Q,0)
        while len(Q)>len(P):
            Empiler(P,0)       
        Empiler(résultat,P[i]+Q[i])
    return résultat

######################################################
# EXERCICE 04
######################################################
def Mult(λ,P):
    '''Fonction qui prend en argument un scalaire sous la forme d’un entier 
    ou d’un flottant(type int or type float), ainsi qu’un polynôme sous la 
    forme d’une liste(type list) et qui retourne en sortie le polynôme 
    (sous la forme d’une liste)(type list) 
    égal au produit du polynôme par le scalaire pris en argument.'''
    polynôme=[]
    for i in range(0,len(P)):
        Empiler(polynôme,λ*P[i])
    return polynôme

######################################################
# EXERCICE 05
######################################################
def Multiplier(P,Q):
    '''Fonction qui prend en argument deux polynômes sousla forme de listes 
    (type list) et qui retourne en sortie le polynôme(sous la forme d’une liste)
    (type list) égal au produit des deux polynômes pris en argument.'''
    LdeL=[]
    #On crée une liste qui servira de liste de liste .
    polynôme=[]
    #On crée la liste polynôme.
    while Premier(P)==0:
        Dépiler(P)
    #On enlève les 0 superflus à la fin de la liste K .
    while Premier(Q)==0:
        Dépiler(Q)
    #On enlève les 0 superflus à la fin de la liste T .
    K=max(P,Q)
    #K est la liste la plus grande entre P et Q .
    T=min(P,Q)
    #T est la liste la plus petite entre P et Q .

    for i in range(len(K)):
    #On crée une boucle où i parcoust l'intervalle [0,(longueur de K)-1]
        Empiler(LdeL,[])
    #à chaque parcours on ajoute une liste dans la liste Ldel.
    #On crée une liste dans la liste où l'on stockera les i-èmes développements
        while len(K+T)>len(LdeL[i]):
            Empiler(LdeL[i],0) 
    #On fait en sorte que chaque sous liste ait la même longueur en terme de 0
    #que la liste représentant le polynôme de plus haut degré possible .
    #Afin que chaque terme soit positionné au bon degré lors de l'addition..
        for p in range(len(T)):
    #Pour p allant de 0 au dernier terme de la liste la plus petite .
            LdeL[i].insert(i+p,K[i]*T[p])
    #Dans la i-ème liste , à la i+p-ième position , on ajoute le produit
    #du i-ème terme de K avec le p-ième terme T .Cela revient donc à créer une
    #i-ème liste modélisant le polynôme issu du produit du i-ème coefficient du
    #polynôme de plus haut degré , avec les p-ième coefficient du polynôme
    #de plus bas degré . 
    for z in range(len(LdeL)):
    #On crée une boucle où z parcours l'intervalle 1 , nombre de terme de LdeL.
        polynôme=Additionner(polynôme,LdeL[z])
    #polynôme ne contenant initialement rien, additionner polynôme avec
    #chacune des sous liste Ldel[z] revient à additionner l'ensemble des
    #sous listes et à obtenir le résultat dans la liste polynôme .
    while Premier(polynôme)==0:
        Dépiler(polynôme)
    #On retire les 0 superflus situés à la fin de la liste polynôme .
    if polynôme==[]:
        Empiler(polynôme,0)
    #si la liste polynôme est vide c'est qu'elle ne contenait que des 0 donc
    #qu'elle représentait le polynôme nul . Le polynôme nul étant usuellement
    #représenté par la liste [0] on transforme la liste polynôme en [0]
    return(polynôme)
    #on renvoie la liste polynôme .
    
######################################################
# EXERCICE 06
######################################################
def Diviser(K,D):
    '''Fonction qui prend en argument deux polynômes sous la forme de listes 
    (type list) et qui retourne en sortie la liste de deux polynôme(type list) 
    dont le premier est le quotient et le deuxième est le reste de la division
    euclidienne de K par D (K et D sont pris en argument) Les polynômes récupérés 
    en sortie seront  également sous la forme de listes(type list).'''
    Ldequotient=[]
    #On crée la liste de listes de quotients.
    quotient=[]
    #On crée la liste contenant le quotient final .
    while Premier(K)==0:
        Dépiler(K)
    #On enlève les 0 superflus à la fin de la liste K .
    while Premier(D)==0:
        Dépiler(D)
    #On enlève les 0 superflus à la fin de la liste D .
    X=len(K)
    #On sauvegarde la longueur de la liste du dividende car nous allons par la 
    #suite modifier ce dividende en reste donc sa longueur variera . Or il nous
    #faudra cette longueur pour mettre suffisament de 0 dans nos listes .
    
    if D==[]:
    #Si D est égal à la liste vide c'est qu'il était égal au polynôme nul .
        return 'Erreur, division par 0'
    #On retourne donc une erreur de division par zéro .
    if K==[]:
    #Si K est la liste vide c'est qu'il était égal au polynôme nul .
        return [[0],[0]]
    #Si le dividende est nul alors le quotient et le reste sont nuls .
    if len(D)>len(K):
    #Si la longueur de D est supérieure à celle de K cela signifie que le 
    #diviseur a un degré supérieur à celui du dividende .
        return [[0],K]
    #on retourne un quotient égal au polynôme nul et un reste égal à K .
    for i in range(len(K)):
    #Pour i allant de 0 à la longueur de K -1 .
        if K==[]:
    #Si K est égal à la liste vide c'est que le reste est nul.
            break
    #On met fin à la boucle car si le reste est nul la division est terminée.
        if len(D)>len(K):
            break
    #Si le degré du diviseur est supérieur à celui du divisé la division 
    #doit s'arrêter .
        Ldequotient.append([])
    #On ajoute une liste vide dans la liste de liste.
        while X>len(Ldequotient[i]):
    #Tant que la longueur de la liste nouvellement créée est inférieure à celle
    #du dividende .
            Ldequotient[i].append(0)
    #On ajoute 0 à la liste nouvellement créée .
        Ldequotient[i].insert(len(K)-len(D),Premier(K)//Premier(D))
    # On insère dans la i-ème liste,en position len(K)-len(D) soit la position 
    #du plus haut terme du dividende moins la position du plus haut terme du 
    #diviseur ,le quotient de la divison euclidienne du plus haut terme 
    #du dividende par le plus haut terme du diviseur .
        K=Additionner(K,Multiplier(D,Mult(-1,Ldequotient[i])))
    #On remplace K par l'addition entre K et (la multiplication entre le 
    #diviseur et (l'opposé de la i-ème partie du quotient)) .
        while Premier(K)==0:
            Dépiler(K)
    #On enlève les 0 superflus dans le reste K .
    for z in range(len(Ldequotient)):
    #on crée une boucle où z réalise un parcourt de 0 à longueur de la liste
    #de quotients -1 .
        quotient=Additionner(quotient,Ldequotient[z])
    #On somme les z-èmes quotients entre eux afin d'obtenir le quotient .
    while Premier(quotient)==0:
        Dépiler(quotient)
    #On enlève les 0 superflus à la fin de la liste quotient .
    if K==[]:
    #Dans le cas où le reste K est la vide c'est qu'il est le polynôme nul .
        K=[0]
    #L'affichage standard du polynôme nul est [0].
    if quotient==[]:
    #Dans le cas où le quotient est la liste vide c'est qu'il est le polynôme nul .
        quotient=[0]
    #L'affichage standard du polynôme nul est [0].
    return [quotient,K]
    #On retourne le quotient et le reste .

######################################################
# EXERCICE 07
######################################################
def PGCD(P,Q):
    '''Fontion qui calcule un PGCD unitaire pour deux polynômes passés en argument 
    sous forme de listes(type list), dont l’un des deux au moins est non nul.'''
    if Q==[0] or Q==[]:
        return P
    else:
        return PGCD(Q,Diviser(P,Q)[1])