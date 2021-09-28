from random import randrange
from math import sqrt
def Premier(k):
    i=2
    b=0
    while  i<=int(sqrt(k)) and b==0 :
        if k%i==0 :
            b=1
        i=i+1
    return b
#############################################
def InterPremier(FI, E) :
    a1=1
    a2=0
    a3=FI
   
    b1=0
    b2=1
    b3=E

    while b3!=0 and b3!=1 :
        q=int(a3/b3)
        t1=a1-q*b1
        t2=a2-q*b2
        t3=a3-q*b3
        a1=b1
        a2=b2
        a3=b3
        b1=t1
        b2=t2
        b3=t3   
    if b3==0 :
        PGCD=a3
        INV=1
        INVERSE=0
    if b3==1 :
        PGCD=b3
        INV=0
        INVERSE=b2
    return (PGCD, INV, INVERSE)
##################################################
stop=0
while stop==0 :
    print("*********************Menu********************")
    print("* 1-Generer une paire de cle.               *")
    print("* 2-Chiffrer un message (cle sauvegarder).  *")
    print("* 3-Dechiffrer un message.                  *")
    print("* 4-Quitter.                                *")
    print("*********************************************")
    operation=int(input("Veuillez Choisir une des operations proposees : "))
    while operation!=1 and  operation!=2 and  operation!=3 and  operation!=4 :
        print("Operation Introuvable!!!")
        operation=int(print("Veuillez Choisir une des operations proposees : "))   
    
    if operation==1 :
        TN=0
        MAX=0
        MIN=1
        a=1
        i=1        
        while TN<=0 :
            TN=int(input("Veuillez introduire la taille de N : "))
        while i<=TN:
            MAX=MAX+(a*9)
            a=a*10
            i=i+1
        i=1
        while i<=TN-1:
            MIN=MIN*10
            i=i+1
################################################################            
        v=1
        while v==1 :
            a=1
            while a==1:
                P=randrange(MAX+1)
                if P!=0 and Premier(P)==0 :
                    a=0
                    b=1
            while b==1:
                Q=randrange(MAX+1)
                if Q!=0 and Premier(Q)==0:
                    if P*Q>=MIN and P*Q<=MAX and P*Q!=1 :
                        b=0
                        v=0
                        N=P*Q
                        
###############################################################                        
        FI=(P-1)*(Q-1)
        
###############################################################
        b=1
        while b==1 :
            E=randrange(2045)
            
            (PGCD, INV, INVERSE)=InterPremier(FI, E)
            if PGCD==1:
                b=0
                D=INVERSE
        print("La cle publique est : ", E)
        print("La cle privee est : ", D)
##############################################################
        stop=int(input("Voullez-vous reessayer? [0/1]"))
        
        
    if operation==2 :
        M=int(input("Veuillez entre le message a chiffre : "))
        y=(M**E)%N
        print ("Le message chiffre : ", y)
        stop=int(input("Voullez-vous reessayer? [0/1]"))
    if operation==3 :
        M=int(input("Veuillez entre le message a dechiffre : "))
        x=(y**D)%N
        print("Le message dechiffre : ", x)
        stop=int(input("Voullez-vous reessayer? [0/1]"))
