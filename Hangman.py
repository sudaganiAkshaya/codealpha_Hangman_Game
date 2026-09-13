import random
# List of predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]
# Select a random word
word = random.choice(words)
# Store guessed letters
guessed_letters = []
# Number of incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0
print("HANGMAN GAME")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")
# Main game loop
while incorrect_guesses < max_attempts:
    # Display the current word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
# Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n Congratulations!")
        print("You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print(" Correct guess!")
    else:
        incorrect_guesses += 1
        print(" Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

else:
    print("\n Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")