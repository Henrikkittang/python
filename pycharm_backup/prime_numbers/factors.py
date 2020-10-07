from math import ceil
import time

inp_num = int(input("Here: "))
primes = []
factors = []
index = 0

t1 = time.time()
def check_prime(num):
    """Check if a number is prime or not"""
    if num == 4:
        return False
    for i in range(2, ceil(num/2) + 1):
        if num % i == 0:
            return False
    return True


for i in range(2, ceil(inp_num/2) + 1):
    """Finds all the prime numbers between 0 and the input number divided by 2"""
    if check_prime(i) == True:
        primes.append(i)

while index < len(primes):
    """Finds the factors by dividing the number on the prime numbers"""
    if inp_num % primes[index] == 0:
        factors.append(primes[index])
        inp_num //= primes[index]
    else:
        index += 1
t2 = time.time()


for i in factors:
    print(i)

print("Program used " + str(t2-t1) + " seconds")
