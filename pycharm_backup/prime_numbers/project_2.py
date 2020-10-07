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
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cant divide by zero")
        return 0


def determineOperator(operation, num1, num2):
    # Determine operation
    if (operation == 1 or operation == '+'):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2 or operation == '-'):
        print("Subtracting...")
        print(sub(num1, num2))
    elif (operation == 3 or operation == '*'):
        print("multiplying...")
        print(mul(num1, num2))
    elif (operation == 4 or operation == '/'):
        print("dividing...")
        print(div(num1, num2))


def main():
    validInput = False
    while not validInput:
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do? add(1), subtract(2), multiply(3), or divide(4) enter:  "))
            validInput = True
        except ValueError:
            print("Invalid input. Try again  ")
        except:
            print("Unknown error")
        determineOperator(operation, num1, num2)


if __name__ == "__main__":
    main()
