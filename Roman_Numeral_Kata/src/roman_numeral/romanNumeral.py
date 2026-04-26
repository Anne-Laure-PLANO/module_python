def convertNumber(number: int) -> str:
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result = ""
    while number > 0:
        for numb, sym in values:
            if number >= numb:
                result += sym
                number -= numb
                break
    return result


def isValidNumber(number: str) -> bool:
    return number.isdigit()


def userNumber() -> int:
    while True:
        number = input("Enter a number:")
        if isValidNumber(number):
            return int(number)
        else:
            print("Please enter a valid number.")


# logique
if __name__ == "__main__":
    userChoice = userNumber()
    result = convertNumber(userChoice)
    print(f"conversion de {userChoice} en chiffre romains : {result}")
