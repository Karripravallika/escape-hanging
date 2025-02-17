import random
from stages import stages
from words import words

def hangman():
    lives = 6
    random_word = random.choice(words)
    display = ['_'] * len(random_word)  
    guessed_letters = set()  

    print("Welcome to Hangman!")
    print(" ".join(display))  

    while lives > 0:
        guessed_letter = input("Guess a letter: ").lower()

        if not guessed_letter.isalpha() or len(guessed_letter) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guessed_letter in guessed_letters:
            print(f"You've already guessed '{guessed_letter}'. Try another letter.")
            continue

        guessed_letters.add(guessed_letter)

        if guessed_letter in random_word:
            for position, letter in enumerate(random_word):
                if letter == guessed_letter:
                    display[position] = guessed_letter  
        else:
            lives -= 1
            print(f"'{guessed_letter}' is not in the word.")
            if lives >= 0:
                print(stages[lives])  

        print(" ".join(display))  

        if '_' not in display:
            print("Congratulations! You win! The word was:", random_word)
            break

        print(f"Lives remaining: {lives}")  

    else:
        print("You lose! The word was:", random_word)

if __name__ == "__main__":
    hangman()

