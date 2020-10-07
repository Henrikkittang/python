def add(num1, num2):
    """returns num1 plus num2"""
    return num1 + num2

def sub(num1, num2):
    """returns num1 minus num2"""
    return num1 - num2

def mul(num1, num2):
    """returns num1 times num2"""
    return num1 * num2

def div(num1, num2):
    """returns num1 divided by num2"""
    return num1 / num2

def perc(num1, num2):
    """finds num1 percentage of num2"""
    return (num1/num2) * 100


def main():
    validInput = False
    while not validInput:
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do? add(1), subtract(2), multiply(3), divide(4) or find percentage of(5) "
                                  "enter:  "))
            validInput = True
        except:
            print("Invalid input. Try again  ")

    # Determine operation
    if (num2 == 0 and operation == 4):
        print("Cant divide by zero ")
        main()
    if(operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif(operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif(operation == 3):
        print("multiplying...")
        print(mul(num1, num2))
    elif(operation == 4):
        print("dividing...")
        print(div(num1, num2))
    elif(operation == 5):
        print("finding percentage...")
        print(perc(num1, num2), "%")


    # Ask user to continue
    loop = input("Do you want to continue? Type yes if so or any other character if not  ")
    if(loop == "yes"):
        main()
    else:
        print("done")


main()
