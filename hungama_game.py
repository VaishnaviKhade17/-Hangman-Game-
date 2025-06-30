import random

# Predefined list of 5 words
word_list = ["apple", "tiger", "robot", "chair", "house"]
secret_word = random.choice(word_list)

# Variables for game state
guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while attempts_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.\n")
        continue
    
    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        print("Incorrect guess.\n")
        attempts_left -= 1

# End of game
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
