def clean(): #variable clean_1
    with open("insultes_clean.txt", "r") as tempfile:
        cleanner = tempfile.read().split("\n")
        for i in cleanner:
            if "" in cleanner :
                cleanner.remove("")
        with open("insultes.new.txt", "w") as tempfiles:
            for item in cleanner:
                tempfiles.write('"'+item+'"'+", ")
        return cleanner
print(clean())

# A la ligne 2 :
# open() ouvre le fichier insultes_clean.txt, il utilise 'r' (read).

# A la ligne 3 :
# J'ai utilisé split() et "\n" qui est le signe de retour chariot. C'est a dire qu'il commence une nouvelle ligne dans l'impression.

# Aux lignes 8 et 11 :
# J'ai utilisé la fonction random.randint et len(). random.randint génére un nombre aléatoire et len() renvoie le nombre des insultes dans la variable list_ins2