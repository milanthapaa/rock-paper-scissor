import random


def rock_paper_scissor():
    print("Welcome to Rock, Paper and Scissor Game")
    possible_values = ["rock", "paper", "scissor"]
    computer = random.choice(possible_values)

    while True:
        user = input("Choose one from Rock, Paper and Scissor").lower()


rock_paper_scissor()
