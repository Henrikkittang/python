from math import sqrt

def loop():
    more = False
    validInput = False
    while not validInput:
        try:
            loop = input("Do you want to calculate more? Type yes or no  ")
            if (loop == "yes"):
                more = True
                validInput = True

            elif (loop == "no"):
                print("Done")
                break

        except ValueError:
            print("Invalid input. Try again ")
        except:
            print("Unknown error")

    if (more == True):
        main()
    else:
        exit()


def main():
    validInput = False
    while not validInput:
        try:
            a = float(input("What is the A value?"))
            b = float(input("What is the B value?"))
            c = float(input("What is the C value?"))
            validInput = True
        except ValueError:
            print("Invalid input, try again   ")
            print()
        except:
            print("Unknown error")

    if(a == 0):
        print("A cant be 0, try again")
        loop()

    if ((b*b) - 4 * a * c < 0):
        print("No solution, try again")
        loop()

    xONE = (b*(-1) + sqrt((b*b)-4*a*c))/(2*a)
    xTWO = (b*(-1) - sqrt((b*b)-4*a*c))/(2*a)

    print("xONE:  ", xONE)
    print("xTWO:  ", xTWO)

    buttomPointX = (xONE + xTWO)/2

    buttomPointY = ((a*buttomPointX)**2)+(b*(buttomPointX))+c

    print("The graph crosses the Y-axis in point (0,",c,")")
    if(a > 0):
        print("Lowest point on the graph is (",buttomPointX,",",buttomPointY,")")
    else:
        print("Highest point on the graph is (",buttomPointX,",",buttomPointY,")")
    print(" ")

    loop()


main()
