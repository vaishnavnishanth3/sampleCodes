import random

thinkingNumber = random.randint(1,100)

difficulty = input("Welcome to Guess Game!\nI'm thinking of a number between 1 and 100.\nChoose Difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    choices = 10
elif difficulty == 'hard':
    choices = 5

print(f"You have {choices} attemps to guess the number! ")

for i in range(choices):
    guessNumber = int(input("Make a Guess: "))
    
    if guessNumber != thinkingNumber:
        if guessNumber > thinkingNumber:
            print("Too High!")
        elif guessNumber < thinkingNumber:
            print("Too Low!")

        choicesLeft = choices-i-1
        
        if choicesLeft != 0:
            print(f"You have {choicesLeft} attempts left to guess the number")
        elif choicesLeft == 0:
            print("You've reached the limit and you failed to guess the number!")

    elif guessNumber == thinkingNumber:
        print("You Guessed it Correct!")
        break