import matplotlib.pyplot as plt 
import numpy as np 

def A(pN,pM, Xi,m):
    p1 = pN-Xi*(pM-pN)
    pm = pM+Xi*(pM-pN)
    A = []
    for i in range (1,m+1):
        new = p1 + (i-1)*(pm-p1)/m
        A.append(new)
    return A

def S(A): 
    S = []
    for i in range (len(A)):
        for j in range (len(A)): 
            S.append([A[i],A[j]])
    return S

def pi1(s): 
    return (s[0]-1)*np.exp(4*(2-s[0]))/(np.exp(4*(2-s[0]))+np.exp(4*(2-s[1]))+1)

def pi2(s): 
    return (s[1]-1)*np.exp(4*(2-s[1]))/(np.exp(4*(2-s[1]))+np.exp(4*(2-s[0]))+1)

def initQwithLargeConstantValue(Q): 
    for i in range (len(Q)):
        for j in range(len(Q[0])):
            Q[i][j]=2
    return Q

#Créer une fonction qui trouve le maximum de Q(s,a)
def trouve_max(Q,s_prime):
    sol = Q[0][s_prime]
    arg = 0
    for i in range (1,len(Q)): 
        if sol <= Q[i][s_prime]:
            sol = Q[i][s_prime]
            arg = i
    return sol, arg   

def epsilon(beta,t):
    #return the value of epsilon at the moment t
    return np.exp(-beta*t)

#current_column_index = index of the price set by the players in t-1
def get_next_action(Q,s_t_index,epsilon,m,trouve_max):
    if np.random.random() < 1-epsilon: 
        return trouve_max(Q,s_t_index)[1]
    else: 
        return np.random.randint(m)
    
def updateQ(Q,S,a_t_index, s_t_index, alpha, delta, pi, s_t1_index):
    Qbis = Q
    for i in range(len(Q)): 
        for j in range(len(Q[0])):
            if i == a_t_index and j == s_t_index: #faire attention à différencier valeurs et indices : ici on parle d'indice
                Qbis[i][j]= (1-alpha)*Q[i][j] + alpha*(pi(S[s_t1_index]) + delta*trouve_max(Q,s_t1_index)[0])
    return Qbis

def find_index(S,s_t): 
    index = -1
    for test in range (len(S)):
        if S[test][0] == s_t[0] and S[test][1]==s_t[1] :
            index = test 
    return index

def jeu(pN,pM,Xi,m, A, S, epsilon, beta, alpha, delta, initQ, updateQ, nb_iteration, get_next_action,trouve_max,pi1,pi2, find_index):
    #Initialisation
    A = A(pN,pM, Xi,m)
    S = S(A)
    Q1 = np.zeros((len(A),len(S))) #Q matrice j1
    Q1 = initQ(Q1)
    Q2 = np.zeros((len(A),len(S))) #Q matrice j2
    Q2 = initQ(Q2)
    s_t_index = np.random.randint(m*m)
    temps = []
    profit = []
    
    #Phase itérative
    for t in range(nb_iteration):
        a_t_index1 = get_next_action(Q1,s_t_index,epsilon(beta,t),m,trouve_max)
        a_t_index2 = get_next_action(Q2,s_t_index,epsilon(beta,t),m,trouve_max)
        #print(a_t_index1,a_t_index2)
        s_t1 = [A[a_t_index1],A[a_t_index2]]
        profit1 = pi1(s_t1)
        s_t1_index = find_index(S,s_t1)
        Q1 = updateQ(Q1,S, a_t_index1, s_t_index, alpha, delta, pi1, s_t1_index)
        #print(Q1[a_t_index1,s_t_index])
        Q2 = updateQ(Q2,S,a_t_index2, s_t_index, alpha, delta, pi2, s_t1_index)
        s_t_index = s_t1_index
        temps.append(t)
        profit.append(profit1)
        
        
    return S[s_t1_index], temps, profit