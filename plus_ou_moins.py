from random import randint

def AskMaxInt() -> int:
    """ Demande un nombre max et le renvoi """
    MaxInt:str = input("\nChoisir le nombre maximum à deviner : ")
    while not MaxInt.isdigit() or not 9 < int(MaxInt) < 65535:
        print("Choisir un nombre pas trop petit (10 minimum)")
        MaxInt:str = input("Choisir le nombre maximum à deviner : ")
    return int(MaxInt)

def AskTries(N:int) -> int:
    """ Demande un nombre d'essai et le renvoi """
    Tries:str = input("\nChoisir le nombre d'essai : ")
    while not Tries.isdigit() or not 0 < int(Tries) <= N/2:
        print("Choisir un nombre d'essai résonable")
        Tries:str = input("Choisir un nombre d'essai : ")
    return int(Tries)

def replay():
    redo:str =  input("\nVeux-tu rejouer ? (oui/non)\n").lower()
    
    while not redo == "oui" and not redo == "non":
            print("\nChoisir 'Oui' ou 'Non'")
            redo:str = input("Veux-tu rejouer ? (oui/non)\n").lower()
            
    if redo == "oui":
        pass
    if redo == "non":
        print(' ')
        exit()

while True:
    MaxInt:int = AskMaxInt()
    Tries:int = AskTries(MaxInt)
    random:int = randint(1, MaxInt)
    
    print("R: ", random)
    print("\nJ'ai choisi un nombre entre 1 et {}".format(MaxInt))
    print("A vous de le deviner en {} tentatives au maximum !\n".format(Tries))
    
    for i in range(Tries):
        print("Essai n° " + str(i+1))
        
        choix:str = input("Votre proposition : ")
        
        while not choix.isdigit():
            print("Il faut choisir un nombre et pas écrire du text !")
            choix:str = input("Votre proposition : ")
            
        if int(choix) < random:
            if i == Tries-1:
                print("\nDommage ! Vous avez perdu \nIl fallait trouvé {}.\n".format(random))
                replay()
                
            else:
                print("Trop petit \n")
                
        if int(choix) > random:
            if i == Tries-1:
                print("\nDommage ! Vous avez perdu \nIl fallait trouvé {}.\n".format(random))
                replay()
                
            else:
                print("Trop grand \n")
                
        if int(choix) == random:
            print("Bravo ! Vous avez trouvé {} en {} essais".format(random,i+1))
            replay()
