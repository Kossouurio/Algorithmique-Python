import Tools
def Game(message: str):
    response: [str] = ["y", "n"]
    while message == "y":
        final_result: str = Tools.Three_Wins_or_Loses()
        print(final_result)
        message = Tools.Response_replay(response)
    print("Merci d'avoir joué !")



Game("y")









