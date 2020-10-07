
def main():
    xONE = float(input("Whats is the first x-coordinate?  "))
    yONE = float(input("Whats is the first y-coordinate?  "))
    xTWO = float(input("Whats is the second x-coordinate?  "))
    yTWO = float(input("Whats is the second y-coordinate?  "))

    Ys = yTWO - yONE
    Xs = xTWO - xONE

    a = Ys/Xs
    b = yTWO-(a*xTWO)

    print("a = ",a)
    print("b = ",b)

    if(b > 0):
        print("f(x)=",a,"x +",b)
    else:
        print("f(x)=",a,"x",b)


main()