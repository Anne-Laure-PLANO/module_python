import random


def userChoice() -> int:
    print("""
    ________________________
      Welcome to Shi-Fu-Mi
    ________________________
    """)
    isGood = False
    while isGood == False:
        userChoice = input("""Enter your choice: 
            1 - Papier
            2 - Caillou
            3 - Ciseaux
        """)
        if userChoice == "1" or userChoice == "2" or userChoice == "3":
            isGood = True
        else:
            print("Please choose between 1, 2 or 3.")
    return userChoice


def pcChoice() -> int:
    return random.randint(1, 3)


def displayChoice(choice) -> str:
    match choice:
        case 1:
            return "Papier"
        case 2:
            return "Caillou"
        case 3:
            return "Ciseaux"


def compareResults(userChoice, pcChoice) -> None:
    result = f"{userChoice}-{pcChoice}"
    if result == "1-2" or result == "2-3" or result == "3-1":
        print("You won!")
    elif userChoice == pcChoice:
        print("draw match")
    else:
        print("you loose")


# Logique


for i in range(3):  # 3parties
    user = int(userChoice())
    print(f"You chose {displayChoice(user)}")

    computerChoice = pcChoice()
    print(f"Computer chose {displayChoice(computerChoice)}")

    compareResults(user, computerChoice)
