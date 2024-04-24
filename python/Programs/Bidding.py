import os

auction = {}

def info():
    name = input("Enter your Name: ")
    bid = int(input("Enter your Bid: $"))
    auction[name] = bid
    
    option = input("\nAre There Any other Bidders? [Yes / No]")

    match(option.upper()):

        case "YES":
            os.system('cls')            
            info()

        case _:
            os.system('cls')
            highest_bid()

def highest_bid():
    greater = 0

    for x,y in auction.items():
        if y > greater:
            winner = x

    print(f"\nThe Auction Winner is {winner}")

info()
