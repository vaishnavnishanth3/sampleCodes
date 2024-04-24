def add(n1,n2):
    return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

for i in operations:
    print(i)

operation = input("Enter the Operation: ")

new_operation = operations[operation]

answer = new_operation(num1,num2)

print(answer)

isProgramFinished = False

while isProgramFinished == False:

    option = input("Type Yes to continue and No to Exit! \n")

    if option == 'Yes':
        isProgramFinished = False
    
    else:
        break

    num2 = float(input("Enter the next number: "))

    operation = input("Enter the Operation: ")

    new_operation = operations[operation]

    answer = new_operation(answer,num2)

    print(answer)
