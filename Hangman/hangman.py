import pyfiglet
from random import choice as random_choice
from collections import deque
import string
import words
from stages import stages
from time import sleep


def validate_letter(letter):
    while letter.lower() not in alphabet:
        letter = input("Please enter a valid letter! ")

    return letter


def check_whole_word(player_word, word_to_guess):
    if player_word.lower() == word_to_guess.lower():
        return True
    return False


def correct(x, hint=False):
    print(x)

    if not hint:
        print("Correct!\n")
        print("Loading...\n")
        sleep(3)
    else:
        print("You used a hint and lost 10 points")
        print("\nLoading...")
        sleep(4)


def wrong():
    print("Wrong!\n")
    print("Loading...")
    sleep(4)


def word_correct(w, x):
    print(w)
    print("You guessed the word!\n")
    if len(x) < 3:
        print("Loading next word...")
        sleep(4)
    else:
        print("Loading...")
        sleep(3)


def letter_reveal(word, letter, index):
    return word[:index] + letter + word[index + 1:]


def hide_letter(word, index):
    return word[:index] + "_" + word[index + 1:]


def play(words_to_guess, stages, points, lost=False):
    for c, w in words_to_guess.items():
        current_category = c
        for current_word in w:
            l_letter = current_word[0]
            r_letter = current_word[-1]
            to_guess_hidden = '_' * len(current_word[1:-1])
            to_guess = current_word[1:-1]
            display_word = f"{l_letter}{to_guess_hidden}{r_letter}"
            word_guessed = False
            hints_left = 1 if len(current_word) < 6 else 3
            hangman_stages = stages[::-1]

            current_stage = hangman_stages.pop()

            while not lost:
                if word_guessed:
                    break
                letter_guessed = False
                hint_used = False
                print_words = ''

                if guessed_words:
                    print_words = f"Guessed words: {', '.join(guessed_words)}"

                print("=" * 70)
                print(f"Stage {len(stages) - len(hangman_stages)}{' ' * 10}", end='')
                print(f"{print_words}")
                print("=" * 70)
                print(*current_stage)

                print(f"\nHints left: {hints_left}\n")
                print(f"Word category: {current_category.capitalize()}")
                print(f"Word to guess: {display_word}\n")
                current_guess = input("Guess (a letter, the whole word, or type hint! to reveal a random character and "
                                      "lose 10 points): ").lower()

                if current_guess == "hint!":
                    if not hints_left:
                        while current_guess == "hint!":
                            print("\nYou have used all available hints for this word.")
                            current_guess = input("Guess (a letter, the whole word, or type hint! to "
                                                  "reveal a random character): ")
                    else:
                        hints_left -= 1
                        points -= 10
                        hint_used = True
                        index_to_reveal = random_choice([i for i, x in enumerate(to_guess_hidden) if x == "_"])
                        reveal_letter = to_guess[index_to_reveal]

                        # to_guess_hidden = to_guess_hidden[:index_to_reveal] + reveal_letter + \
                        #                   to_guess_hidden[index_to_reveal + 1:]

                        to_guess_hidden = letter_reveal(to_guess_hidden, reveal_letter, index_to_reveal)
                        to_guess = hide_letter(to_guess, index_to_reveal)
                        display_word = f"{l_letter}{to_guess_hidden}{r_letter}"

                        if check_whole_word(display_word, current_word):
                            guessed_words.append(current_word)
                            word_guessed = True

                if len(current_guess) == 1:
                    current_letter_guess = validate_letter(current_guess)

                    for i in range(len(to_guess)):
                        if to_guess[i] == current_letter_guess:
                            letter_to_reveal = to_guess[i]

                            to_guess = hide_letter(to_guess, i)

                            to_guess_hidden = letter_reveal(to_guess_hidden, letter_to_reveal, i)
                            display_word = f"{l_letter}{to_guess_hidden}{r_letter}"
                            letter_guessed = True
                            break

                elif len(current_guess) == len(current_word) and not current_guess == "hint!":
                    if check_whole_word(current_guess, current_word):
                        guessed_words.append(current_word)
                        word_guessed = True

                if check_whole_word(display_word, current_word):
                    guessed_words.append(current_word)
                    word_guessed = True

                if word_guessed:
                    word_correct(current_word, guessed_words)
                    break
                if len(current_guess) > len(current_word) or not letter_guessed and not current_guess == "hint!":
                    wrong()
                    current_stage = hangman_stages.pop()
                    if not hangman_stages:
                        print(*current_stage)
                        return False, points
                else:
                    correct(display_word, hint_used)
                print()

    return True, points


def generate_words(player_category):
    if player_category == '4':
        for c in words.words:
            word_category = words.words_categories[c]
            add_word = random_choice(words.words[c])
            player_words_to_guess[word_category] = [add_word]

    else:
        word_category = words.words_categories[player_category]
        player_words_to_guess[word_category] = []
        while len(player_words_to_guess[word_category]) < words_to_guess_counter:
            add_word = random_choice(words.words[player_category])
            if add_word not in player_words_to_guess[word_category]:
                player_words_to_guess[word_category].append(add_word)


def select_category(player_category):
    while player_category not in words.words and not player_category == '4':
        player_category = input(f"Please enter a valid category (1 to {categories_count}): ")

    generate_words(player_category)


def start_print():
    print(f"{pyfiglet.figlet_format('W e l c o m e   t o H a n g m a n!', font='big')}\n"
          f"\nRules:\nYou start with {player_points} points.\n"
          f"Guess letters one by one or guess the whole word (a-Z, case insensitive).\n"
          f"Reveal a random letter by typing hint! instead of a letter to help you guess a word. Every hint reduces "
          f"your points by 10.\n"
          f"You get 1 hint for short words (words with 5 or less symbols) and 3 for longer ones.\n"
          f"The first and the last letters of the word will be revealed.\n"
          f"The hints and the hangman stages reset with each word.\n"
          f"Each new stage (8 total) comes after a failed guess.\n"
          f"You lose if you fail to guess a word.\n"
          f"Guess {words_to_guess_counter} words and keep as many points as you can!\n"
          f"\nGood luck!\n")
    print("Please select a category\n"
          "1: Sport\n"
          "2: Music\n"
          "3: Geography (cities)\n"
          "4: Mixed")


words_to_guess_counter = 3  # with the option to extend
player_points = words_to_guess_counter * 30
categories_count = len(words.words) + 1
alphabet = string.ascii_lowercase
player_words_to_guess = {}
words_categories = deque()
guessed_words = []

start_print()
category = input(f"Enter a number (1 to {categories_count}): ")
select_category(category)

game = play(player_words_to_guess, stages, player_points)

print()
print("=" * 70)
if game[0]:
    print("Congratulations! You've won!")
    print(f"Points left: {game[1]}")
else:
    print("Sorry, you lost the game")

if guessed_words:
    print(f"Guessed words: {', '.join(guessed_words)}")

print("=" * 70)
