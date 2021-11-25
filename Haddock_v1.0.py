import random #importe au hasard
def VocabulaireGrossierPirate():
    list_insult = []
    with open("insultes.new.txt", "r", encoding="UTF-8") as tempfile:
        fichier = tempfile.readline().split(", ")
    for listeInsultes in fichier:
        list_insult.append(listeInsultes)
    i = random.randint(9,len(list_insult))
    chc = list_insult[i]
    print("numero de l'insulte : ", i)
    return chc[1:len(chc)-1]
print(VocabulaireGrossierPirate())

# A la ligne 4 :
# open() ouvre le fichier insultes.new.txt, il utilise 'r' (read).
# j'ai ajouté l'encodage UTF-8, pour qu'il n'y est pas d'erreur d'affichage de caractère par la suite.

# A la ligne 5 :
# J'ai utilisé split() pour ajouter une virgule ainsi qu'un espace pour délimiter les insultes.

# Aux lignes 8 et 11 :
# J'ai utilisé la fonction random.randint et len(). random.randint génére un nombre aléatoire et len() renvoie le nombre des insultes dans la variable list_insult.
# J'ai utilisé return pour la variable chc (choice) et j'ai entré l'entier 1 pour qu'à l'affichage final, l'insulte ne soit pas délimité.
