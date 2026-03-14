import random

# List of predefined words
words = ["python", "coding", "intern", "project", "developer"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
tries = 6

# Create blank display
display = ["_"] * len(word)

print("Welcome to Hangman Game")

while tries > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        tries -= 1
        print("Wrong Guess. Tries left:", tries)

if "_" not in display:
    print("\nYou Won! The word was:", word)
else:
    print("\nYou Lost! The word was:", word)
