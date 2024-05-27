import random
from words import words_list

def choose_word():
    """Selects a random word from the list and returns it in uppercase."""
    return random.choice(words_list).upper()

def display_hangman(remaining_attempts):
    """Returns a visual representation of the hangman state based on remaining attempts."""
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[remaining_attempts]

def play_game(selected_word):
    """Main logic for the Hangman game."""
    word_display = "_" * len(selected_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    remaining_attempts = 6

    print("Let's play Hangman!")
    print(display_hangman(remaining_attempts))
    print(word_display)
    print("\n")

    while not guessed and remaining_attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in selected_word:
                print(guess, "is not in the word.")
                remaining_attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_display)
                indices = [i for i, letter in enumerate(selected_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_display = "".join(word_as_list)
                if "_" not in word_display:
                    guessed = True
        
        elif len(guess) == len(selected_word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != selected_word:
                print(guess, "is not the word.")
                remaining_attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_display = selected_word
        else:
            print("Not a valid guess.")
        
        print(display_hangman(remaining_attempts))
        print(word_display)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + selected_word + ". Maybe next time!")

def main():
    """Runs the game and offers to play again."""
    selected_word = choose_word()
    play_game(selected_word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        selected_word = choose_word()
        play_game(selected_word)

main()
