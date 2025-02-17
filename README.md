# 🎲 escape-hanging 🎲
Welcome to the classic Hangman game built with Python! Try to guess the hidden word one letter at a time. But beware, each wrong guess brings
you closer to the hangman!
## 📌 Features
### 🔠 Random word selection from a predefined list.
### 🚫 Input validation to allow only letters.
### 🔄 Tracks guessed letters to avoid repetition.
### 💀 Hangman stages that appear as lives decrease.
### 🎉 Win by guessing the word before you run out of lives!

## ⚙️ Prerequisites 
##### Python 3.x

## 🚀 Installation
##### main.py: The main game logic.
##### stages.py: Contains the hangman figure stages.
##### words.py: Contains the list of words.

## 🎮 How to Play
#### 1.Run the game:
  ###### python main.py
#### 2. Guess the hidden word by entering one letter at a time.
#### 3.✅ If the letter is in the word, it appears in the correct position(s).
#### 4.❌ If the letter is incorrect, you lose a life, and the hangman figure gets closer to completion.
#### 5.The game ends when:
  ###### 🎉 You correctly guess the word.
  ###### 💀 You run out of lives.

  ##  📚 Example Gamep
  ####  _ _ _ _ _ _
  ####  Guess a letter: e
  ####  _ _ _ _ e _
  ####  Guess a letter: a
 ####   'a' is not in the word.
  ####  Lives remaining: 5

  



