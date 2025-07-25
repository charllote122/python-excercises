import random

# List of possible words
word_list = ["python", "hangman", "challenge", "programming", "developer"]

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game variables
display = ["_" for _ in range(word_length)]
lives = 6
guessed_letters = []

print("Welcome to Hangman Game!")

# Game loop
while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong! You lost a life. Lives left: {lives}")

    print("Current word:", " ".join(display))

# Game over conditions
if "_" not in display:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("You lost! The word was:", chosen_word)
