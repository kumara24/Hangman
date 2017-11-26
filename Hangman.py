import random


WORD_LIST = [
    
    'friend',
    'encyclopedia',
    'alacrity',
    'burgeon',
    'deleterious',
    'euphemism',
    'ogle',
    'robust',
    'alchemy',
    'deiberate',
    'levity',
    'olfactory',
    'potable',
    'tranquil',
    'alibi',
    'buttress',
    'evacuate',
    'ominous',
    'potent',
    'rotund',
    'transcribe',
    'allay',
    'ruse',
    'trangress',
    'transient',
    'aloof',
    'lithe',
    'trivial'
    
]


HANGMAN = (
    """
    *-------*
    """,
    """
    *-------*
    |
    |
    |
    |
    """,
    """
    *-------*
    |       |
    |       0
    |
    |
    """,
    """
    *-------*
    |       |
    |       0
    |       |
    |
    """,
    """
    *-------*
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    *-------*
    |       |
    |       0
    |      /|\\
    |      /
    """,
    """
    *-------*
    |       |
    |       0
    |      /|\\
    |      / \\
    """
)


MAX = len(HANGMAN) - 1
ALPHABETH = 'abcdefghijklmnopqrstuvwxyz'


def guess_letter(letters_guessed):
    while True:
        guess = input('Guess a letter: ').lower()
        if guess not in ALPHABETH:
            print (guess, 'is not in the alphabet, try again!')
        elif guess in letters_guessed:
            print ('You already guessed {}'.format(guess))
        else:
            return guess

word_to_guess = random.choice(WORD_LIST)

def play_hangman():
    hang_size = 0
    word_to_guess_spaced = ' '.join(word_to_guess)

    hidden = ['_']*len(word_to_guess)

    letters_guessed = set()
    user_guessed_word_spaced = ' '.join(hidden)

    

    while hang_size < MAX:

        print
        print (user_guessed_word_spaced)

        user_guess = guess_letter(letters_guessed)
        letters_guessed.add(user_guess)

        if user_guess in word_to_guess:

            print ("{} is in the word".format(user_guess))

            for i, letter in enumerate(word_to_guess):
                if user_guess == letter:
                    hidden[i] = letter

            user_guessed_word_spaced = ' '.join(hidden)
            if user_guessed_word_spaced == word_to_guess_spaced:
                print
                print (word_to_guess)
                break

        else:
            print ("{} is not in the word".format(user_guess))
            hang_size += 1
            print (HANGMAN[hang_size])

    return user_guessed_word_spaced == word_to_guess_spaced


if __name__ == '__main__':

    print ("H A N G M A N!")
    print ("Learn SAT Vocab without any of the bore!")
    choice2 = 'y'

    while choice2 == 'y':
        print("\n")
        choice = input("Do you want to add words to the game? (y or n): ")

        if choice == 'y':
            print ("Type 'null' to stop adding words: ")
            addition = input();
            while addition != 'null':
                WORD_LIST.append(addition)
                addition = input()
            
        is_winner = play_hangman()
    
        if is_winner:
            print ('\nYou win! Good job!!!')
            choice2 = input('Do you want to play again? (y or n): ')
        else:
            print ('\nGAME OVER')
            print ('The word was ' + word_to_guess)
            choice2 = input('Do you want to play again? (y or n): ')

    input("Good Bye!")
