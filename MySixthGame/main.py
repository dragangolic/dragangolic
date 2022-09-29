import random
from words import words
import string

user_input = input('Type something')


def get_valid_word(words):
    word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in word
    alphabet = set(str(string.ascii_uppercase))
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have guessed these letters: ', ' '.join(used_letters))

        # what current word is ( ie W - RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)


            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You lost, sorry. The word was', word)
    else:
        print('You won', word, 'is correct!')


hangman()



