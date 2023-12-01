def print_result(ordinateur, j, player, ia):
    # Définition des résultats possibles et des conséquences sur les scores
    results = {
        # 1er colonne pour la réponse de l'ordinateur, la 2nd pour la réponse fournie par le joueur
        # Comparaison des données fournie par l'ordinateur et du joueur pour afficher la réponse correcte et le bon ajout de points        ("Pierre", 'Pierre'): ("Égalité", 0, 0),
        ("Pierre", 'Feuille'): ("Victoire", 1, 0),
        ("Pierre", 'Ciseaux'): ("Perdu", 0, 1),
        ("Feuille", 'Pierre'): ("Perdu", 0, 1),
        ("Feuille", 'Feuille'): ("Égalité", 0, 0),
        ("Feuille", 'Ciseaux'): ("Victoire", 1, 0),
        ("Ciseaux", 'Pierre'): ("Victoire", 1, 0),
        ("Ciseaux", 'Feuille'): ("Perdu", 0, 1),
        ("Ciseaux", 'Ciseaux'): ("Égalité", 0, 0),
        ("Pierre", 'p'): ("Égalité", 0, 0),
        ("Pierre", 'f'): ("Victoire", 1, 0),
        ("Pierre", 'c'): ("Perdu", 0, 1),
        ("Feuille", 'p'): ("Perdu", 0, 1),
        ("Feuille", 'f'): ("Égalité", 0, 0),
        ("Feuille", 'c'): ("Victoire", 1, 0),
        ("Ciseaux", 'p'): ("Victoire", 1, 0),
        ("Ciseaux", 'f'): ("Perdu", 0, 1),
        ("Ciseaux", 'c'): ("Égalité", 0, 0),
    }
    # Récupération du résultat du match et des incrémentations des scores
    result, player_inc, ia_inc = results.get((ordinateur, j), ("", 0, 0))

    # Mise à jour des scores du joueur et de l'ordinateur
    player += player_inc
    ia += ia_inc

    # Affichage du résultat du match
    print(result)

    # Affichage des scores actuels
    print(f"Joueur: {player} / {ia} :Machine")

    # Retour des scores mis à jour
    return player, ia


def ask_input(message: str, authorized_inputs: list) -> str:
    # Boucle de saisie pour vérifier que l'utilisateur entre une valeur autorisée
    while True:
        # Saisie de l'utilisateur
        value: str = input(f"{message} ({'/'.join(authorized_inputs)}): ")

        # Vérification si la saisie est comprise dans authorized_inputs
        if value in authorized_inputs:
            # Retour de la valeur
            return value
        else:
            # Afficher un message d'erreur si la saisie n'est pas comprise dans authorized_inputs
            print(f"Veuillez entrer une lettre parmi {', '.join(authorized_inputs)}.")
