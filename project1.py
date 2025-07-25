# Rock wins against scissors
# Scissors wins against paper
# Paper wins against rock

def play_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


# Get input from both players
print("Welcome to Rock, Paper, Scissors!")
print("Choices: rock, paper, scissors")

player1 = input("Player 1, enter your choice: ").lower()
player2 = input("Player 2, enter your choice: ").lower()

# Validate input choices
valid_choices = ["rock", "paper", "scissors"]

if player1 not in valid_choices or player2 not in valid_choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
    result = play_game(player1, player2)
    print(result)
