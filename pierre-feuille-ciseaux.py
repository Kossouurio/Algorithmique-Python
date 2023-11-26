#   pierre-feuille-ciseaux

from random import randint

choiceList: list = ["1","2","3"]

Yes_No_List: list = ["oui", "non"]

AnswerList = [
    [["Égalité !", 0], ["Perdu !", 0], ["Gagné !", 1]],
    [["Gagné !", 1], ["Égalité !", 0], ["Perdu !", 0]],
    [["Perdu !", 0], ["Gagné !", 1], ["Égalité !", 0]]
]

def Ask_Choice(allowed_choices: list[str]) -> str :
    message: str = "Choisir entre : "
    for i in allowed_choices:
        message += str(i) + "  "
        
    while True:
        choice: str = input(message+"\n").lower()
        if choice in allowed_choices:
            return choice
    
        print("Erreur\n")

def Check_Answer(chosen_number: int, chosen_random_number: int, result: int) -> str:
    """Check the answer

    Args:
        chosen_number (int): Number chosen by the user.
        chosen_random_number (int): Number chosen by the computer.
        result (int): Is a "0" or a "1", "0" for ["Égalité !" "Perdu !" "Gagné !"] and "1" for the score corresponding to.
    """
    return AnswerList[chosen_number-1][chosen_random_number-1][result]

def AskInt(Text: str) -> int:
    while True:
        Integer: str = input( Text + "\n")

        if Integer.isdigit():
            return int(Integer)

        print("Erreur\n")

def Game():
    while True:
        print("\nBienvenu sur le jeu du pierre feuille ciseaux ")
        
        score: int = 0
        
        number: int = AskInt("Quel est le nombre de manches nécessaires pour désigner le gagnant?")
        
        while number:
            print("\nPierre = 1, Feuille = 2 et Ciseaux = 3")
            choice: int = int(Ask_Choice(choiceList))

            randomInt: int = randint(1,3)

            print(Check_Answer(choice, randomInt, 0))
            
            score += Check_Answer(choice, randomInt, 1)
                
            number -= 1
            
        print("\nTu as fini avec un score de {}".format(score))
        
        print("Souhaites-tu rejouer ?")
        question = Ask_Choice(Yes_No_List)
        if question == "non":
            break


Game()