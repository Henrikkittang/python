import random


def guess_the_number():
    print()
    print("Try to guess the number between 1 and 100. The program will tell you if you should guess higher or lower")
    random_num = random.randint(1, 100)
    guess_count = 1
    guess = False
    while not guess:
        guesse_num = int(input("Guess a number: "))
        if (guesse_num > 100 or guesse_num < 1):
            print("Only numbers between 1 and 100")
            return
        elif (guesse_num > random_num):
            print("The number is smaller")
            guess_count += 1

        elif guesse_num < random_num:
            print("The number is greater")
            guess_count += 1

        elif guesse_num == random_num:
            print("You guessed correct! You used",guess_count,"tries")
            again = input("Do you want to try again? Type y if so  ")
            if again == "y":
                guess_the_number()
            else:
                exit()


guess_the_number()
