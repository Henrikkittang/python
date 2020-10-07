import random


def life_check(opponent_life, player_life):
    if (opponent_life == 0):
        print("You won!")
        exit()
    elif (player_life == 0):
        print("You lost!")
        exit()


def rock_paper_scissor():
    print("Best of three")
    moves = ["rock", "paper", "scissor"]
    opponent_life = 3
    player_life = 3
    game1 = True
    while game1:
        life_check(opponent_life, player_life)
        opponent = moves[random.randint(0, 2)]
        player = input("Choose rock, paper or scissor: ")
        game2 = True
        while game2:
            test = player + opponent
            if (player == opponent):
                print()
                print("Tie")
                break

            elif(test == "rockscissor" or  test == "paperrock" or test == "scissorpaper"):
                print()
                print("Opponent choose:", opponent)
                print("You won this round")
                opponent_life -= 1
                break

            elif(test == "rockpaper" or test == "scissorrock" or test == "paperscissor"):
                print()
                print("Opponent choose:", opponent)
                print("Opponent won this round")
                player_life -= 1
                break

            else:
                print("Try again")
                rock_paper_scissor()
                break


rock_paper_scissor()


