# demander choix valide(min, max):
#   while True:
#       choix = intput("c quoi ton choix")
#       if choix pas un nombre 
#           return false
#       if choix entre min et max
#           return choice
#       else :
#           message d'erreur "..."

def demander_choix_valide(min,max):
    while True :
        choix = input("Faites votre choix : ")
        if choix.isdigit():
            choix = int(choix)
            if min <= choix <= max:
                return int(choix)
        else :
            print("Veuillez saisir un choix valide !")