import random #importe au hasard
def VocabulaireGrossierPirate():
    with open("insultes.new.txt", "r", encoding="UTF-8") as tempfile:
        txt = tempfile.read().split(", ")
        chc = random.choice(txt)
        return chc[1:len(chc)-1]
print(VocabulaireGrossierPirate())

# A la ligne 3 :
# open() ouvre le fichier insultes.new.txt, il utilise 'r' (read).
# j'ai ajouté l'encodage UTF-8, pour qu'il n'y est pas d'erreur d'affichage de caractère par la suite.

# A la ligne 4 :
# J'ai utilisé split() pour ajouter une virgule ainsi qu'un espace pour délimiter les insultes.

# A la ligne 5 :
# J'ai utilisé la fonction random.choice qui choisis une insulte au hasard dans la variable txt.

# A la ligne 6 :
# J'ai utilisé return pour la variable chc (choice) et j'ai entré l'entier 1.

