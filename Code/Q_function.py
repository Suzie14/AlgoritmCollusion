import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt



def pi(p_i,p_j): 
    return (p_i-1)*np.exp(4*(2-p_i))/(np.exp(4*(2-p_i))+np.exp(4*(2-p_j))-1)

def A(pN,pM, Xi,m):
    p1 = pN-Xi*(pM-pN)
    pm = pM+Xi*(pM-pN)
    A = [p1]
    for i in range (1,m):
        new = p1 + (i-1)*(pm-p1)/(m-1)
        A.append(new)
    return A
        
def S(p_i,p_j):
    return [p_i,p_j]    



Q[0] = np.zeros(m,m**(n*k))
#Créer une fonction qui trouve le maximum de Q(s,a)
def trouve_max(Q,s_prime):
    sol = Q[0][s_prime]
    for i in range (2,len(Q)): 
        if sol <= Q[i][s_prime]:
            sol = Q[i][s_prime]
    return sol
#A initialiser (Par exemple set tout à 1 ou qqchose comme ça)
#A chaque fois j'ai un a_t et un s_t associé au moment t : 
#J'update Q[t] = et la je change juste la valeur en a_t et en s_t 
#=> Plus ingénieux de créer une première fonction en mode : updateQ
def updateQ(Q,a_t,s_t, alpha, delta, pi_t, s_t1):
    Qbis = Q
    for i in range(len(Q)): 
        for j in range(len(Q[0])):
            if i == a_t and j == s_t: #faire attention à différencier valeurs et indices : ce n'est pas le cas ici 
                Qbis[i][j]= (1-alpha)*Q[i][j] + alpha*(pi_t + delta*trouve_max(Q,s_t1))

    return Qbis





 


def updateQ(Q,s,a, alpha):
    Q[s][a]
    i = 0
    if a(t-1)= a(t):
        i = i+1
    else : 
        i = 0
    if i < 100000: 
        if a = a_t and s = s_t
            Q[t]= (1-alpha)*Q[t-1] + alpha...
        else : 
            Q[t]= Q[t-1]
            
    else : 
        return Q[t]
