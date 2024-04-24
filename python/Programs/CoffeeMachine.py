print("1.Expresso\n2.Latte\n3.Cappuccino")

coffeeDict = {
    'expresso' :
                {
                    'Water': 50,
                    'Coffee': 18,
                    'Milk': 0,
                    'Price': 1.50
                },
    'latte': 
                {
                    'Water': 200,
                    'Coffee': 24,
                    'Milk':150,
                    'Price':2.50
                },
    'cappuccino' :
                {
                    'Water':250,
                    'Coffee':24,
                    'Milk':100,
                    'Price': 3.00
                },
}

water = 300
milk = 300
coffee = 200

penny = 0.01
dime = 10 * penny
nickel = 5 * penny
quarter = 25 * penny

def report(water,milk,coffee,waterofCoffeeType,coffeeofCoffeeType,milkofCoffeeType):

    if water - waterofCoffeeType < 0 or coffee - coffeeofCoffeeType < 0 or milk - milkofCoffeeType < 0:
        return False

    else:
        return True

def main(water,milk,coffee):
    coffeeType = input("What would you like? (expresso/latte/cappuccino): ")

    priceofCoffeeType = coffeeDict.get(coffeeType).get('Price')
    waterofCoffeeType = coffeeDict.get(coffeeType).get('Water')
    coffeeofCoffeeType = coffeeDict.get(coffeeType).get('Coffee')
    milkofCoffeeType = coffeeDict.get(coffeeType).get('Milk')

    pennies = float(input("How many pennies? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickel? "))
    quarters = float(input("How many quarters? "))

    penniesTotal = pennies * penny
    dimeTotal = dimes * dime
    nickelTotal = nickels * nickel
    quarterTotal = quarters * quarter

    totalAmount = penniesTotal + dimeTotal + nickelTotal + quarterTotal

    if totalAmount >= priceofCoffeeType:
        totalAmount -= priceofCoffeeType

        reportF = (report(water,milk,coffee,waterofCoffeeType,coffeeofCoffeeType,milkofCoffeeType))

        if reportF:
            water -= waterofCoffeeType
            milk -= milkofCoffeeType
            coffee -= coffeeofCoffeeType

            print(f"\nReport:\nMilk: {milk}\nWater: {water}\nMilk: {milk}\n")
            print(f"Have {coffeeType} for ${priceofCoffeeType} and get remaining ${int(totalAmount)}")
        
        else:
            print("Insufficient Ingredients")
    
    elif totalAmount < priceofCoffeeType:
        print("Not Sufficient Amount!")


main(water,milk,coffee)