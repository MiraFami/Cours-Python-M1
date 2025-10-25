# 22000002 Paul Machin
# 22503743 FAMI Zoumirath 


# Section 1 : les imports

from P01_utils import lire_donnees
from P01_utils import visualiser_donnees
import math as mt 
import numpy as np

# Section 2

X,y=lire_donnees(100) #données d'entrainements 
X_test,y_test=lire_donnees(10)
print(X[:5])
print(y[:5])


# visualiser_donnees(X,y,X_test)

# retourne la distance euclidienne.

def dist (X_i , X_j):
    sum_d=0
    for i in range (len(X_i)):
     
     res_1=(X_i[i]-X_j[i])**2
     sum+=res_1
    return mt.sqrt(sum_d)


#fonction permettant d’obtenir les indices des 𝑘 plus proches voisin d’un individu de test parmi le jeu d’entraînement

def indices_k_voisins(X_train,X_test_i,k):
    distances=[]
    for individu_train in X_train:
        distance=dist(X_train,X_test_i)
        distances.append(distance)
        indices_tries=np.argsort(distances)
        
    return indices_tries[:k]      
     
    
#calcule la classe la plus représentée dans la liste   

def classe_plus_presente(k_classes):
    class_plus_represente="F"
    if k_classes.count("H")>k_classes.count("F"):
        class_plus_represente="H"
    
    
    return class_plus_represente    

#Implémentez une fonction k_plus_proches_voisins_liste 


def k_plus_proches_voisins_liste(X_train,y_train,X_test,k):
    if k==None:
       k=1 
    predictions=[]  
    
    for X_test_i in X_test:
        indices=indices_k_voisins(X_train,X_test_i,k) # les indices des individus du jeu d'entrainement
        classes_indices=[] # pour determiner la classe de l'elemnt se trouvant à indices i F ou H
        for indice in indices :
            classes_indices.append(y_train[indice])
    
    
      #la classe predite sera la classe plus represente(presente) de k.classes
        classe_predite=classe_plus_presente(classes_indices)      
        predictions.append(classe_predite)
        
    return  predictions   
    
    
