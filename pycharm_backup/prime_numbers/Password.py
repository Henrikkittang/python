import time
import random

neighbour_hack_count = 0
lucky_chance = 3


def intro():
    print("Ok, so you want to be a hacker?")
    print("I will show you have to be a hacker")
    print("Before you can begin to hack stuff, you need to make an account at hacker.com")
    print()
    make_user()


def make_user():
    valid_password_1 = False
    while not valid_password_1:
        try:
            password_1 = int(input("Type a four digit number as your password: "))
            valid_password_1 = True
        except ValueError:
            print("Make sure your password is a number")
            print()
        except:
            print("Something went wrong. Try again")
            print()
            make_user()


    if password_1 >= 1000 and password_1 <= 9999:
        valid_password_2 = False
        while not valid_password_2:
            try:
                password_2 = int(input("Double check your password: "))
                valid_password_2 = True
            except ValueError:
                print("Make sure your password is a number")
                print()
            except:
                print("Something went wrong. Try again")
                print()
                make_user()
        if password_1 != password_2:
            print("Your passwords did not match. Please type your password again")
            print()
            make_user()
        else:
            type_password(password_1)
    else:
        print("Make sure your password is a four digit number. Please type your password again")
        print()
        make_user()


def brute_force(skill_level, money, beefy_computer, password, return_address, hack_count):
    index = 1000
    loop = True
    while loop:
        if index == password:
            print(index)
            print()
            print("Password broken. Entering user profile")
            loop = False
        else:
            index += 1

    if return_address == "neighbour":
        brute_forced = True
        hack_neighbour(skill_level, money, beefy_computer, brute_forced, hack_count)




def type_password(password):
    valid_password_1 = False
    while not valid_password_1:
        try:
            password_check = int(input("Type your password to enter your user: "))
            valid_password_1 = True
        except ValueError:
            print("Make sure your password is a number")
            print()
        except:
            print("Something went wrong. Try again")
            print()
            make_user()

    if password_check != password:
        print("Your password is incorrect. Please try again")
        print()
        type_password(password)
    else:
        print("Your password is correct")
        user()


def user():
    print("Great, you have made an account. Soon you will be ready to hack")
    print("You would want to hack someone with a lot of money")
    print("The more money you get, they more you can upgrade you gear and skills")
    skill_level = 1
    money = 0
    beefy_computer = 1
    print()
    print("Currently you have no skills, you have no money and your computer is crap")
    print("Type i to see your stats")
    print("You need to do something about this. You need to hack or scam someone")
    hack_count = 0
    hack(skill_level, money, beefy_computer, hack_count)


def neighbour_counter_attack(skill_level, money, beefy_computer, hack_count):
    right_answer = 0
    equations = [input("x^2 = 3^2 + 4^5. x = "), input("x^2 - 13 > 2.  x > "),
                 input("4^-1 * 4^2 + 3. Write as simple as possible: ")]
    for eq in range(0, 2):
        answer = equations[eq]
        if answer == "5" and eq == 0 or answer == "4" and eq == 1 or answer == "7" and eq == 2:
            right_answer += 1

    if right_answer >= 2:
        print()
        print("You managed to defeat your neighbour")
        print("As a surrender gift he gave you his kid's collage founds")
        print("That's adds up to a nice, round sum of 20 000")
        print("You also received 2 skill level xp")
        money += 20000
        hack_count += 3

    else:
        print()
        print("Your neighbour fucked you over there and trust me his is pissed")
        print("He managed to take almost half of your money")
        money -= money//2

    hack(skill_level, money, beefy_computer, hack_count)


def hack_neighbour(skill_level, money, beefy_computer, brute_forced, hack_count):
    global neighbour_hack_count
    if skill_level == 1 and beefy_computer == 1:
        neighbour_hack_count += 1
        print("You don't have a beefy enough computer to brute force his password yet so you will have to hack him")
        print("Solve these equations to access his child porn (those things sells like gold on the black market)")
        print()
        if neighbour_hack_count == 1:
            eq = input("x/3 * 4 = 108:  ")
        if neighbour_hack_count == 2:
            eq = input("x = 1/2 * 8 * 2*sqrt(3) * sqrt(3)/2. x =")

        if eq == "81" and neighbour_hack_count == 1:
            hack_count += 1
            print("Congrats, you successfully retrieved your neighbour porn")
            print("A guy named Hebert bought it for 10 000 dollars")
            money += 10000

        elif eq == "12" and neighbour_hack_count == 2:
            print("You found one of your neighbour's saving accounts")
            print("3000 was added to your account")
            money += 300

        else:
            print("Wrong answer")

        hack(skill_level, money, beefy_computer, hack_count)

    if not brute_forced and beefy_computer == 2:
        if skill_level == 2 and neighbour_hack_count > 3:
            input("With a better computer, you are now able to brute force your way into your neighbour's computer")
            neighbour_password = random.randint(1000, 9999)
            return_to_neighbour = "neighbour"
            brute_force(skill_level, money, beefy_computer, neighbour_password, return_to_neighbour, hack_count)
        else:
            print("You will have to improve your skill level in order to hack your neighbour again")
            hack(skill_level, money, beefy_computer, hack_count)

    elif brute_forced and beefy_computer == 2:
        neighbour_hack_count += 1
        if neighbour_hack_count == 3:
            print("Your neighbour is fucking tired of being black mailed and have decided to hack you back")
            print("You will have to do a little quick math to counter attack him")
            neighbour_counter_attack(skill_level, money, beefy_computer, hack_count)
        else:
            hack_count += 1
            print("You now have access to his whole computer")
            input("You should take advantage of this and black mail him for money")
            add_money = random.randint(2000, 3000)
            money += add_money
            print(str(add_money) + " was added to your account")
            hack(skill_level, money, beefy_computer, hack_count)


def scam(skill_level, money, beefy_computer, hack_count):
    global lucky_chance
    scam_selector = input("You can choose between e-mail, facebook, or phone bot scam. Type 1, 2 or 3")
    hack_count += 1
    if skill_level == 1:
        print("You are only in skill level 1 so your scam wont be that great")
        if scam_selector == "1":
            print("Good, now lets send out those E-mails")
            add_money = random.randint(150, 300)
        elif scam_selector == "2":
            print("Facebook scams completed")
            add_money = random.randint(300, 500)
        elif scam_selector == "3":
            print("Phone bots on their way")
            add_money = random.randint(100, 200)
        else:
            print("You need to input 1, 2, 3")
            scam(skill_level, money, beefy_computer, hack_count)

    if skill_level == 2:
        print("You are in skill level 2 so your scams will be a little better")
        if scam_selector == "1":
            print("Good, now lets send out those E-mails")
            add_money = random.randint(600, 800)
            lucky_chance += 1
        elif scam_selector == "2":
            print("Facebook scams completed")
            add_money = random.randint(500, 700)
        elif scam_selector == "3":
            print("Phone bots on their way")
            add_money = random.randint(700, 900)
        else:
            print("You need to input 1, 2, 3")
            hack(skill_level, money, beefy_computer, hack_count)
        lucky_chance += 1

    if random.randint(0, 100) < lucky_chance:
        print("A local millionaire bought one of your scams")
        print("Loan your stocks to me and receive tripled the amount you invested in under three weeks!!!) ")
        print("and you now receive 8000 easy bucks ")
        money += 8000
        lucky_chance = 0
        hack(skill_level, money, beefy_computer, hack_count)

    money += add_money
    print(str(add_money) + " was added to your account")
    hack(skill_level, money, beefy_computer, hack_count)

    # add the other skill levels


def hack(skill_level, money, beefy_computer, hack_count):
    global neighbour_hack_count
    print()
    target = input("Do you want to hack a big cooperation, your neighbour or make a scam?")
    print()

    if hack_count == 6 and skill_level == 1:
        print("You have now hacked enough to upgrade your skill level")
        skill_level += 1
        hack(skill_level, money, beefy_computer, hack_count)

    if target == "i":
        print("skill_level:", skill_level)
        print("Balance: ", money)
        print("beefy computer level:", beefy_computer)
        hack(skill_level, money, beefy_computer, hack_count)

    elif target == "cooperation" and skill_level < 3 and beefy_computer < 3:
        print("You need to be in skill level 3 and have a computer at level 3")
        hack(skill_level, money, beefy_computer, hack_count)
    elif target == "neighbour":
        print("Your neighbour is fucking poor but ok")
        brute_forced = False
        hack_neighbour(skill_level, money, beefy_computer, brute_forced, hack_count)
    elif target == "scam":
        print("Whyyyyy")
        scam(skill_level, money, beefy_computer, hack_count)
    elif target == "purchase":
        if beefy_computer == 1:
            upgrade = input("Do you want to upgrade to a beefier computer? It will cost you 25 000. Type y if so")
            if upgrade == "y" and money > 25000:
                money -= 25000
                beefy_computer += 1
                neighbour_hack_count = 0
                print("Your current balance is now " + str(money))
                print("Your computer is now in level 2 ")

            elif upgrade == "y":
                print("You need " + str(25000 - money) + " more money")

            else:
                print("Ok then")
            hack(skill_level, money, beefy_computer, hack_count)

        if beefy_computer == 2 and money > 75000:
            upgrade = input("Do you want to upgrade to a beefier computer? It will cost you 75 000. Type y if so")
            if upgrade == "y":
                money -= 25000
                beefy_computer += 1
                print("Your current balance is now " + str(money))
                print("Your computer is now in level 3 ")
                hack(skill_level, money, beefy_computer, hack_count)

            else:
                print("Ok then")
                hack(skill_level, money, beefy_computer, hack_count)

    else:
        print("You need to chose a real option: cooperation, neighbour, scam, purchase or i")
        hack(skill_level, money, beefy_computer, hack_count)


intro()
