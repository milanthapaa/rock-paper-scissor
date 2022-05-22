import random


def rock_paper_scissor():
    print("Welcome to Rock, Paper and Scissor Game")
    possible_values = ["rock", "paper", "scissor"]
    computer = random.choice(possible_values)

    while True:
        user = input("Choose one from Rock, Paper and Scissor: ").lower()
        if computer == "rock" and user == "rock":
            print("TRY AGAIN!")
        elif computer == "rock" and user == "scissor" or \
                computer == "scissor" and user == "paper" or \
                computer == "paper" and user == "rock":
            print("COMPUTER WON!")
            break
        else:
            print("YOU'VE WON!")
            break


rock_paper_scissor()
