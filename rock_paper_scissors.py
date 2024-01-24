import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""

print("Choose (r)ock, (p)aper or (s)cissors:", end = " ")
players_choice = input()

if players_choice == "r":
    players_choice = rock
elif players_choice == "p":
    players_choice = paper
elif players_choice == "s":
    players_choice = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if players_choice == computer_move:
    print("Draw!")
elif (players_choice == rock and computer_move == scissors) or (players_choice == paper and computer_move == rock) or (players_choice == scissors and computer_move == paper):
    print("You win!")
else:
    print("You lose :-(")
