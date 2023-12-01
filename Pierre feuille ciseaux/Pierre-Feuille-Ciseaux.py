import random
# Import des fonctions ask_input et print_result depuis le fichier tools
from tools import ask_input, print_result


# Définition de la fonction de jeu
def game():
    # Initialisation des scores du joueur et de l'IA
    player: int = 0
    ia: int = 0

    # Boucle de jeu pour les manches gagnants
    while player < 3 and ia < 3:
        # L'ordinateur choisit aléatoirement entre Pierre, Feuille et Ciseaux
        ordinateur: str = random.choice(['Pierre', 'Feuille', 'Ciseaux'])

        print("La Pierre peut être écrite 'p'.")
        print("La Feuille peut être écrite 'f'.")
        print("Le Ciseaux peut être écrit 'c'.")

        # Choix du joueur récupérer avec ask_input
        j: str = ask_input("Veuillez entrer une valeur parmi", ["Pierre", "Feuille", "Ciseaux", "p", "f", "c"])

        # Affichage des résultats avec print_result
        player, ia = print_result(ordinateur, j, player, ia)

    print("Fin du jeu.")

    # Demande au joueur s'il veut recommencer ou non
    restart: str = ask_input("Voulez-vous recommencer ?", ["y", "n", "Y", "N"])
    if restart == "y" or restart == "Y":
        game()
    else:
        print("Merci d'avoir joué.")


# Appel de la fonction de game() pour commencer le jeu
game()
