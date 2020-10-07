print("Collatz \o/")

print("Du skal velge et tall.")

print("Deretter følger vi reglene:")

print("    1. Dersom tallet er et partall, deler vi på to.")

print("    2. Dersom tallet er et oddetall, ganger vi med 3 og legger til 1")

print("Så starter vi på nytt.")

n = int(input("Velg et tall: "))

a = n

print(n)

stego = 0

stegp = 0

while n != 1:

    if(n%2 == 0):

        stegp += 1

        n = n//2

        print(n)

    else:

        stego += 1

        n = 3*n + 1

        print(n)

steg = stegp + stego

print("Når man starter på",a, "bruker man", steg,"steg på å nå 1.")

print("På veien til 1 er man innom", stegp, "partall, og", stego, "oddetall.")