import sys 
def afficher_rectangle(largeur, hauteur):
    if largeur < 1 or hauteur < 1:
        print("Veuillez fournir des valeurs de largeur et de hauteur supérieures ou égales à 1.")
        return

    ligne_horizontale = "o" + "-" * (largeur - 2) + "o"

    print(ligne_horizontale)

    for _ in range(hauteur - 2):
        print("|" + " " * (largeur - 2) + "|")

    if hauteur > 1:
        print(ligne_horizontale)

def main():

    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        largeur = int(sys.argv[1])
        hauteur = int(sys.argv[2])

    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction ma_fonction pour découper la chaîne en utilisant des espaces comme séparateurs
    result = afficher_rectangle(largeur, hauteur)
    
    print(result)

if __name__ == "__main__":
    main()
