# Hangman game - It randomly choose a word from the list and ask user to guess all letters in the word one at a time. For every wrong letter guess user looses one live 

import random


# the word list to use the 'word_list' from hangman_words.py and assign it to a variable called chosen_word.
# Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You have guessed {guess} already. Please guess another letter")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong. If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."    
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess} is not in the word. You have {lives} lives remaining")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
