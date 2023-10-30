import random

print("-----------ROCK PAPER SCISSORS GAME----------")

user_score = 0
comp_score = 0
ties = 0

name = input("enter your name:")
print("""
Rule:
1.Paper vs Rock --> Paper
2.Rock vs scissors --> Rock
3.Scissors vs paper --> Scissors""")
print("""Choices are "
1. Rock
2. Paper
3. Scissors""")

choice = int(input("enter your choice (1-3):"))
             
while choice > 3 or choice < 1:
    choice = int(input("enter valid input: "))

if choice == 1:
    user_choice = "Rock"
elif choice == 2:
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print("The user's choice is:", user_choice)
print("Now it is computer's turn")

computer = random.randint(1, 3)

if computer == 1:
    comp_choice = "Rock"
elif computer == 2:  # Changed "choice" to "computer"
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"

print("The computer's choice is", comp_choice)

if ((user_choice == "Paper" and comp_choice == "Rock")) or ((user_choice == "Rock" and comp_choice == "Paper")):
    print("Paper wins")
    result = "Paper"
elif ((user_choice == "Scissors" and comp_choice == "Rock")) or ((user_choice == "Rock" and comp_choice == "Scissors")):
    print("Rock wins")
    result = "Rock"
else:
    print("Scissors wins")
    result = "Scissors"

if user_choice == comp_choice:
    print("It's a tie")
    result = "tie"

print(f"Result: {result}")

# You might want to add the scoring logic here and ask if the user wants to play again.
