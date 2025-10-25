
def si_annee_bissextile(annee):
    isBissextile = True;
    
    if (annee % 4 == 0):
        if (annee % 100 != 0):
            isBissextile = True;
        else:
            if (annee % 400 == 0):
                isBissextile = True;
            else:
                isBissextile = False;
    else:
        isBissextile = False;

    return isBissextile


def nbre_de_jours(mois,annee):
 if mois>=1 and mois<=12:
    if mois==2:
       if si_annee_bissextile(annee):
         return 29
       else:
         return 28
    else:
     if mois%2==0:
        return 30
     else:
        return 31
 else:
   return 0
  

def affiche(nom,nombre):
  return nom*nombre


def function(s,prefix):
  return  s.count(prefix)


replique_1_2 = "Je ne vous jette pas la pierre , Pierre ,"
replique_2_2 = "  mais j'étais à deux doigts de m'agacer"
replique=replique_1_2+replique_2_2
y=replique.lower()
x=y.split()


#Section

print (si_annee_bissextile(2020))
print (nbre_de_jours(2,2020))
print (affiche("cahier",4))
print(function('je manje', 'je'))
print(replique)
print(len(replique))
print(replique.lower())
print(replique.find("jette"))
print(replique.replace("agacer","enerver"))
print(x)
print(x.count("pierre"))

import math as mt
x=100
print(mt.sin(x))

import datetime
def calcul_age(annee,mois,jours):
  annee_actuelle=datetime.datetime.now()
  annee_naissance=datetime.datetime(annee,mois,jours)
  x=(annee_actuelle-annee_naissance)
  return (x.total_seconds()//(365*24*3600))
  
print(calcul_age(1998,1,9)) 


 
# print(f"karine a {x} ans ")
# print(x.seconds)
# print(x.days)
# print(x.total_seconds()//(365*24*3600))