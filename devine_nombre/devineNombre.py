import random


def initGame():
    print("""
    ______________________________
    Bienvenue sur Devine-Nombre !
    ______________________________
    
    Tentez de trouver le nombre choisi par l'ordinateur le plus rapidement possible.
    Ce nombre est un entier, et est compris entre 1 et 100.
       
    """)


def pcChoice() -> int:
    return random.randint(1, 100)


def userChoice() -> int:
    while True:
        answer = input(" Indiquez votre choix (entre 1 et 100)\n")
        if answer.isdigit():
            answer = int(answer)
            if answer >= 1 and answer <= 100:
                return answer
            else:
                print("Erreur : merci de saisir un nombre entre 1 et 100\n")
        else:
            print("Erreur : merci de saisir un nombre.\n")


def isWin(pc: int, user: int) -> bool:
    if pc == user:
        return True
    else:
        return False


def displayHelp(pc, user):
    if user > pc:
        print("Le nombre choisi est trop grand.")
    else:
        print("Le nombre choisi est trop petit.")


def endGame(score: int) -> None:
    print(f"""
    Félicitations, vous avez gagné !
    Nombre de tentatives réalisées : {score}
    """)
    SystemExit(0)


def increaseAndDisplayScore(score: int) -> int:
    score += 1
    print(f"Nombre de tentatives : {score}")
    return score


# Logique du jeu

initGame()
pc = pcChoice()
score = 0
result = False
while result == False:
    user = userChoice()
    result = isWin(pc, user)
    if result == False:
        displayHelp(pc, user)
        score = increaseAndDisplayScore(score)

endGame(score)
