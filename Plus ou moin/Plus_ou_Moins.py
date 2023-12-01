import Tools


def Game(message: str):
    response: [str] = ["y", "n"]
    while message == "y":
        nb_AI: int = Tools.Get_random()
        essai: int = 10
        while True:
            essai = essai - 1
            nb: int = Tools.Ask_only_number("Donner un nombre: ")
            result: str = Tools.More_or_Less(nb, nb_AI, essai)
            print(result, "(il vous reste", str(essai), "essai)")

            if result == "Victoire" or result == "Perdu":
                message: str = Tools.Response_replay(response)
                break
    print("Merci d'avoir joué !")


Game("y")
