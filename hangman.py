import random

word_list = ["Shearer", "Beckham", "Henry", "Rooney", "Drogba", "Cantona",
    "Lampard", "Gerrard", "Aguero", "Kane", "Scholes", "Vieira",
    "VanPersie", "Bergkamp", "Ronaldo", "Salah", "Hazard", "Terry",
    "Ferdinand", "DeGea", "Pogba", "Ozil", "Mane", "Sterling",
    "Fabregas", "Silva", "Toure", "Giggs", "Vardy", "LeTissier",
    "Zola", "Suarez", "Wright", "Tevez", "Lukaku", "Sane", "Robben",
    "Modric", "Essien", "Bale", "Keane", "Yorke", "Schmeichel",
    "Kompany", "Alonso", "Cole", "Carrick", "Makalele", "Torres",
    "Son", "Grealish"]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list).upper()

chosen_word_char = list(chosen_word)

word_length = len(chosen_word)

num_wrong_tries = 0

guess_list = []

previous_tries = []

while num_wrong_tries < 6 and not all(item in guess_list for item in chosen_word_char):
    guess = input("Select a letter: ")
    if guess.upper() in previous_tries:
        print("You already tried this letter")
    else:
        previous_tries.append(guess.upper())
        if guess.upper() in chosen_word_char:
            print("Correct Letter")
            guess_list.append(guess.upper())
        else:
            print("Wrong Letter")
            num_wrong_tries += 1

    print(stages[6 - num_wrong_tries])

    for char in chosen_word_char:
        if char.upper() in chosen_word_char and char.upper() in guess_list:
            print(char.upper(), end = " ")
        else:
            print("_", end = " ")

    print(f"{6 - num_wrong_tries}/6 Lives Remaining")
    if num_wrong_tries == 6:
        print("GAME OVER")
        print(f"The correct answer was {chosen_word}")

    if all(item in guess_list for item in chosen_word_char):
        print("YOU WIN")
