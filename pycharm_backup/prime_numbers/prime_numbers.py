import math


def main():
    input_value = False
    while not input_value:
        try:
            num = int(input("Check a number: "))
            input_value = True
        except ValueError:
            print("Not an integer. Try again")
            print()
        except:
            print("Unknown error")

    valid_prime = False
    if (num == 4 or num == 1):
        valid_prime = True

    elif(num < 0):
        print("Please input number over 0")
        main()

    for index in range(2, math.ceil(num/2)):
        if(num%index == 0):
            valid_prime = True
            break

    if(valid_prime == True):
        print("It is not a prime number")
    else:
        print("It is a prime number")

    print()
    loop = input("Do you want to check another number? Type y to continue or any other character to end the program ")
    if(loop == "y"):
        main()
    else:
        print("Done")
        exit()
main()

