from database import db

#afficher menu():
#   nouvelle partie
#   quitter le jeux

def afficher_menu():
    print("1. Nouvelle Partie")
    print ("2. Quitter")

#afficher heros()
#   recuperer liste heros de la db
#   afficher liste heros
#   return heros

def afficher_heros(heros):
    for i, p in enumerate(heros, start=1):
        print(f"{i}. Nom : {p.get('nom')} | PV : {p.get('PV')} | ATK : {p.get('ATK')} | DEF : {p.get('DEF')}")
    return heros

#afficher_heros_en_vie()
#   vivants = equipe en vie()
#   pour chaque membre vivant 
#       print membre

#afficher equipe()
#   afficher equipe

def afficher_equipe(equipe):
    print("Équipe :", ", ".join(p["nom"] for p in equipe))

# afficher monstre()
#   afficher monstre

#afficher etat tour()
#   print(nb wave)
#   print(nom equipe)
#   afficher monstre()
#   afficher equipe()