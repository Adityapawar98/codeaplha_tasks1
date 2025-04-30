import random

def choose_word():
    # You can expand this list or load from a file
    word_list = ['python', 'hangman', 'programming', 'challenge', 'developer', 'function']
    return random.choice(word_list)

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           |
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           |
        '''
    ]
    return stages[6 - tries]

def play_game():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    guessed_word = ['_' for _ in word]

    print("Welcome to Hangman!")

    while tries > 0 and set(guessed_word) != word_letters:
        print(display_hangman(tries))
        print("Word: ", ' '.join(guessed_word))
        print("Guessed letters: ", ' '.join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            print("Correct guess!\n")
        else:
            tries -= 1
            print("Incorrect guess.\n")

    if set(guessed_word) == word_letters:
        print("Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(0))
        print("Game over. The word was:", word)

if __name__ == "__main__":
    play_game()
