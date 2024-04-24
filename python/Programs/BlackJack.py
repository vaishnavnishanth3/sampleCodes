import random

def playGame():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    userCardList = []
    computerCardList = []

    randomCard1 = random.choice(cards)
    randomCard2 = random.choice(cards)
    randomCard3 = random.choice(cards)
    randomCard4 = random.choice(cards)
    randomCard5 = random.choice(cards)

    userCardList.append(randomCard1)
    userCardList.append(randomCard2)

    computerCardList.append(randomCard3)

    print(f"Your Cards: {userCardList}")
    print(f"Computer Cards: {computerCardList}")

    userSum = 0

    for card in userCardList:
        userSum += card
    
    if userSum < 16:
        print("Sum is less than 16, You should take another card.")
        userCardList.append(randomCard5)

    elif userSum >= 16 and userSum <= 21:
        option = input("Do you want to take the card or pass it? Type 'y' to Take and 'n' to Pass: ")

        match(option):
            case "y":
                userCardList.append(randomCard5)

            case "n":
                pass

    userSum = 0
    computerSum = 0

    for card in userCardList:
        userSum += card

    for card in computerCardList:
        computerSum += card

    print(f"Computer Cards: {computerCardList}")

    if userSum > 21:
        print("Your Sum is greater than 21! Computer Wins!")

    elif userSum > 16 and userSum > computerSum:
        print("You Won!")

    elif userSum > 16 and userSum < computerSum:
        print("Computer Won!")
    
    elif userSum < 16:
        print("Error!")

def startGame():
    start = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

    if start == 'y':
        playGame()
        startGame()

    elif start == 'n':
        pass

startGame()
