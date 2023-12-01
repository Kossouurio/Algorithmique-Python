import random

RESULTS: list[list[str]] = [
    ["Egalité", "Défaite", "Victoire"],
    ["Victoire", "Egalité", "Défaite"],
    ["Défaite", "Victoire", "Egalité"]
]

POSSIBILITIES: list[str] = ["p", "f", "c"]
WIN_LOSE_GAME: list[str] = ["Vous avez perdu la partie.","Vous avez gagné la partie."]

def Response_replay(list: [str]):
    while True:
        answer: str = input("Voulez vous rejouer ? (y/n) : ").lower()
        if answer in list:
            return answer
        print("Erreur")


def Ask_only_number(message: str):
    while True:
        value: str = input(message)

        if value.isdigit():
            return int(value)

        print("Erreur")


def Ask_Min_Max():
    while True:
        min: int = Ask_only_number("Donnez un nombre minimum: ")
        max: int = Ask_only_number("Donnez un nombre maximum: ")

        if min < max:
            return min, max
        print("Erreur")


def Get_random():
    (a, b) = Ask_Min_Max()
    nb_AI: int = random.randint(a, b)
    return nb_AI


def More_or_Less(a: int, b: int, c: int):
    if c == 0:
        value: str = "Perdu"
    elif a < b:
        value: str = "Plus"
    elif a > b:
        value: str = "Moins"
    else:
        value: str = "Victoire"
    return value


def Ask_PFC(message: str) -> int:
    list_choice: [str] = ["p", "f", "c"]
    while True:
        value: str = input(message).lower()
        while value in list_choice:
            return list_choice.index(value)
        print("Erreur")


def Get_random_PFC():
    nb_AI: int = random.randint(0, 2)
    return nb_AI


def Three_Wins_or_Loses() -> str:
    rounds: list = []

    while rounds.count("0") != 3 and rounds.count("1") != 3:
        result: int = Play()
        rounds.append(str(result))
        print("Wins:", str(rounds.count("1")) + "/3")
        print("Loses:", str(rounds.count("0")) + "/3")
    last_result: int = int(rounds[len(rounds)-1])
    return WIN_LOSE_GAME[last_result]



def Value_result(value: str):
    list_result: [str] = ["Défaite", "Victoire", "Egalité"]
    return list_result.index(value)


def Play() -> int:
    choice_user: int = Ask_PFC("Choisissez entre (Pierre:p, Feuille:f, Ciseaux:c): ")
    choice_AI: int = Get_random_PFC()
    result: str = RESULTS[choice_user][choice_AI]
    print(result,"Choix de l'ordi:", POSSIBILITIES[choice_AI])
    win_lose: int = Value_result(result)
    return win_lose


