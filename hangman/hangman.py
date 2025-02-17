import random
import stages
from words import words

lives = 6
random_word = random.choice(words)
print(random_word)
display = ['_'] * len(random_word)  
print(" ".join(display))  

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    
    if not guessed_letter.isalpha():
        print("Invalid input! Please enter a letter.")
        continue

    
    if guessed_letter in display:
        print(f"You've already guessed '{guessed_letter}'")
        continue

    if guessed_letter in random_word:
        for position in range(len(random_word)):
            if random_word[position] == guessed_letter:
                display[position] = guessed_letter  
    else:
        lives -= 1
        print(f"'{guessed_letter}' is not in the word.")
        if lives < 0:
            print("You lose! The word was:", random_word)
            break
        if 0 <= lives < len(stages.stages):
            print(stages.stages[lives])  
        else:
            print("No more stages left.")

    print(" ".join(display))  

    if '_' not in display:
        game_over = True
        print("You win! The word was:", random_word)

    print(f"Lives remaining: {lives}")
