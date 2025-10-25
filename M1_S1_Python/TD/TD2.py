# Section 1 : Imports de module


# Section 2 : Définition de fonctions

# def compte_mots(phrase:str):
#     s=phrase.split() 
#     return len(s)   


# def est_un_fichier_texte(nom_fichier):
#     if nom_fichier.endswith(".txt") or nom_fichier.endswith(".csv") or nom_fichier.endswith(".json"):
#         return True
#     else:
#         return False



# def table_multiplication(base,mult_d,mult_f):
#     for i in range(mult_d,mult_f+1):
#         print(f'{base}*{i}='+str(base*i))


# def table_de 

# # Section 3 : Tests de fonctions définies et manipulations en mode "script
# print(compte_mots("je vais à l'ecole"))
# print (est_un_fichier_texte("TD.py"))        
# print (est_un_fichier_texte("TD.txt")) 

# table_multiplication(2,1,3)   
   

# def table_de_multiplication(base,multd,mult_f):
#     for i in range (multd,mult_f+1):
#      print (f"{base}*{i}="+str (base*i) )  


# def fonction(LET,s):        
#    s.split()
#    return s.count(LET)


# def fonction(A,s):        
#    s.split()
#    return s.count(A)
 

# print(fonction("A","je vais AAAAA  l'ecole"))

# def annees_production():
#     n_grains = 0
#     for i in range(64):
#         n_grains=n_grains+( 2 ** i)
#         # n_grains += 2 ** i
    
#     masse_annuelle = 650 * 10 ** 6 * 10 ** 6
#     n_grains_par_an = masse_annuelle / 0.035
    
#     return n_grains / n_grains_par_an

# for i in range(10):
#     # print('',i)
#     i+=1
#     print(i)

def argmax(liste):
    ele_grand=liste[0]
    indice_grand=0
    for i,elem in enumerate(liste):
        if elem>ele_grand:
            ele_grand=elem
            indice_grand=i
    return indice_grand        
    

print(argmax([1, 6, 2]))

# def intersect(liste1,liste2):
#   return(liste1+liste2)

# print(intersect([1,2,3],[1,4,5]))

# for i in range(0, 10):
#   print("i")

x = 10
for v in [1, 3, 5]:
  x = x + v 
print(x)


 
 
