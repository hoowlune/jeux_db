from affichage import afficher_heros
from affichage import afficher_equipe
from demander_choix_valide import demander_choix_valide
from database import db

#selectionner heros()
#   tant que equipe !=3
#       afficher heros()
#       demander choix valide(1,len(heros))
#       appliquer choix utilisateur
#       supprimer hero choisi
#       afficher equipe()
#   return equipe

def selectionner_heros():
    equipe = []
    heros = list(db["personnages"].find({}, {"_id": 0}))
    while len(equipe) < 3:
        afficher_heros(heros)
        choix = demander_choix_valide(1,len(heros))
        equipe.append(heros[choix - 1])
        heros.pop(choix - 1)
        afficher_equipe(equipe)
    return equipe

