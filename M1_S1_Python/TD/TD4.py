# Section 1 : Imports de module










# Section 2 : Définition de fonctions

def normalise_texte(texte):
    dico = {
    "À": "A", "Â": "A", "Æ": "A", "Ç": "C", "É": "E", "È": "E", "Ê": "E", "Ë": "E",
    "Î": "I", "Ï": "I", "Ô": "O", "Œ": "O", "Ù": "U", "Û": "U", "Ü": "U", "Ÿ": "Y",
    "à": "a", "â": "a", "æ": "a", "ç": "c", "é": "e", "è": "e", "ê": "e", "ë": "e",
    "î": "i", "ï": "i", "ô": "o", "œ": "o", "ù": "u", "û": "u", "ü": "u", "ÿ": "y"
    }

    chaine_miniscule=''
    for caractere in texte:
        resultat=dico.get(caractere,caractere)
        chaine_miniscule+=resultat

    return chaine_miniscule.lower()


def occurence(chaine):
    dict={}
    mots=chaine.split()
    for mot in mots:
        compteur=mots.count(mot)
        dict[mot]=compteur # ajouter une valeur à un dictionnaire 




    return dict


def det_mot_plus_frequent(chaine): 
    dict=occurence(chaine)
    mot_plus_frequent=None
    val_max=0
    for clé,val in dict.items():
        if val>val_max:
            val_max=val
            mot_plus_frequent=clé
            
            
    return mot_plus_frequent        
    
     
     
# def societe(ventes):
#     nb_total_ventes=0
#     for val in ventes.values():
#         nb_total_ventes+=val
        

#     return nb_total_ventes 

def det_max_ventes(ventes):
    nom_vendeur_max=''
    for nom, nb_articles in ventes.items():
        if nom_vendeur_max=='':
            nom_vendeur_max=nom
        if nb_articles>ventes[nom_vendeur_max]:
            nom_vendeur_max=nom
    
    
    return nom_vendeur_max


def liste_triee_sans_doublon(l_entree):
    nouvelle_version=sorted(list(set(l_entree)))
    
    
    
    
    return nouvelle_version



def element_distinct(liste):
    nb_elements=len(set(liste))
    
    return nb_elements


def pangramme(phrase):
    si_pangramme=True
    if len(set(phrase))==27:
        si_pangramme=True
    else:
        si_pangramme=False    
    
    
    
    return si_pangramme



# Section 3 : Tests de fonctions définies et manipulations en mode "script

# texte_normalise = normalise_texte('Dès Noël où un zéphyr haï me vêt de glaçons würmiens, je dîne d’exquis rôtis de bœuf au kir à l’aÿ d’âge mûr et cætera!')
# print(texte_normalise)
# print(occurence('je je je je vais vais londres '))

# print(occurence('je je je vqaids vais vais '))
# print(societe(ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":2}))
# print(det_max_ventes(ventes={"Dupont":14, "Hervy":19, "Geoffroy":21, "Layec":21}))
# print(pangramme("Portez ce vieux whisk au juge blond qui fume"))
print(det_mot_plus_frequent("jd je je je je eje je eje test ira lequel dire now"))
