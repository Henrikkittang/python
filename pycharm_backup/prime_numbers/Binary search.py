import math

num = int(input("Input a number between 1 and 1000: "))
print("The program wil now try to guess your number with as few attempts as possible")

guess = 500
computer_num = 500
attempts = 0

run = True
while run:
    attempts += 1
    if guess >= 2:
        guess = math.ceil(guess/2)
    print(computer_num, guess)
    if computer_num == num:
        print("The program used " + str(attempts) + " attempts")
        run = False
    elif computer_num > num:
        computer_num -= guess
    elif computer_num < num:
        computer_num += guess
