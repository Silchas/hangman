import random

with open('hangman.txt', 'r') as f:
    words = f.read().splitlines()
    secret_word = random.choice(words)
    letters_guessed = []

    failure_count = 6
    
    while failure_count > 0:
        try:
            guess = input('Enter a letter: ')
            if len(guess) != 1:
                raise ValueError("Please enter only one letter at a time.")
            if not guess.isalpha():
                raise ValueError("Please enter a letter from the alphabet.")
            guess = guess.lower()
            if guess in letters_guessed:
                raise ValueError(f"You have already guessed the letter {guess}.")
        except ValueError as e:
            print(e)
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Correct! {failure_count} more guesses left!")
        else:
            failure_count -= 1
            print(f"Incorrect. {failure_count} turns left!")
        
        wrong_letter_count = 0

        for letter in secret_word:
            if letter in letters_guessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(f"\nCongratulations! The secret word was: {secret_word}. You win!")
            break
    
    else:
        print(f"\nSorry, Try Again. The secret word was: {secret_word}.")
