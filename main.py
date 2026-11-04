import os
from affichage import afficher_menu
from demander_choix_valide import demander_choix_valide
from selectionner_heros import selectionner_heros

# main():
#   afficher le menu()
#   choix = demander choix valide(1,2)
#   appliquer choix utilisateur()

def main():
    afficher_menu()
    choix = demander_choix_valide(1,2)
    appliquer_choix_utilisateur(choix)

# appliquer choix utilisateur():
#   if le choix est 1 
#       nouvelle partie()
#   if le choix est 2
#       quitter_le_jeu()

def appliquer_choix_utilisateur(choix):
    if choix == 1 :
        nouvelle_partie()
    if choix == 2:
        quitter_le_jeu()


#nouvelle partie():
#   clear terminal
#   selectionner_heros()
#   nom equipe = input "Quelle est le nom de votre équipe ? : "
#   lancer vague()

def nouvelle_partie():
    #os.system("clear")
    selectionner_heros()
    nom_equipe = input ("Qu'elle est le nom de votre équipe ? : ")
    #lancer_vague()

#lancer vague
#   nb wave = 0
#   while equipe en vie()
#       nb wave +=1
#       monstre random()  
#       while monstre en vie() et equipe en vie()
#          afficher_etat_tour()
#          combat()
#       si not equipe en vie()
#           game over

def quitter_le_jeu():
    quit()

main()