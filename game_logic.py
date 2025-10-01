import random
from ascii_art import STAGES

# List of secret words (with more words in the pot)
WORDS = ["python", "git", "github", "snowman", "meltdown", "manifold", "secret",
         "random", "trial", "display", "progress", "game", "state", "welcome",
         "book", "bag", "house", "university", "institute", "fan", "mother"
        ]


def get_random_word():
    """selecting a random word from the list."""
    try:
        if WORDS:
            return random.choice(WORDS)
        else:
            print("No words in the list")
            return None
    except Exception as e:
        print(f"Error is {e}")
        return None


def display_game_state(mistakes, secret_word, guessed_letters):
    """displaying the current game state including snowman and word progress."""
    print("*" * 80)
    try:
        if STAGES:
            print(STAGES[mistakes])
        else:
            print(f"snowman stages is empty")
    except Exception as e:
        print(f"Error is {e}")

    try:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Mistakes:", mistakes, "/", len(STAGES) - 1)
        print("\n")
    except Exception as e:
        print(f"Error is {e}")


def play_game():
    """main game loop with enhanced guessing logic."""
    try:
        secret_word = get_random_word()
        if not secret_word:
            return False
    except Exception as e:
        print(f"Error is {e}")
        return False

    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("*" * 80)
    print("Welcome to Snowman Meltdown!")
    print("Save the snowman by guessing the word before it melts completely!\n")

    try:
        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            #getting valid guess from user
            while True:
                guess = input("Guess a letter: ").lower().strip()
                if len(guess) == 1 and guess.isalpha(): #catches single-letter and alphabet
                    if guess in guessed_letters:
                        print("You already guessed that letter! Try again.\n")
                    else:
                        break
                else:
                    print("Please enter a single english letter 'between A to Z'.\n")

            #adding guess to guessed letters
            guessed_letters.append(guess)

            #checking if guess is correct
            if guess in secret_word:
                print("Correct guess!\n")
            else:
                mistakes += 1
                print("Wrong guess! Be careful! The snowman is melting...\n")

            #checking if player won
            won = all(letter in guessed_letters for letter in secret_word)
            if won:
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Congratulations! You saved the snowman!")
                print(f"The word was: {secret_word}")
                return True

    except Exception as e:
        print(f"Error during gameplay {e}")
        return False

    #Player_lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game Over! The snowman melted completely.")
    print(f"The word was: {secret_word}")
    return False


def ask_replay():
    """asking whether the user wants to replay the game."""
    while True:
        try:
            response = input("Do you want to play again? (y/n): ").lower()
            if response in ['y', 'yes', 'yeah', 'yep']:
                return True
            elif response in ['n', 'no', 'nope', 'nah']:
                return False
            else:
                print("Please enter a valid response (y/n).")
        except Exception as e:
            print(f"Error is {e}")


