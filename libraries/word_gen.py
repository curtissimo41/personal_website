# -----------------------------------------------------------------------------
# -----------------------------------Imports-----------------------------------
# -----------------------------------------------------------------------------
import random  # for generating random numbers
import string  # for string operations


# -----------------------------------------------------------------------------
# ------------------------------------Classes----------------------------------
# -----------------------------------------------------------------------------
class CreatedWord:
    upvotes = 0
    downvotes = 0

    def __init__(self, word, definition, example):
        self.word = word
        self.definition = definition
        self.ex_sent = example


# -----------------------------------------------------------------------------
# -----------------------Helper Functions (Alphabetized)-----------------------
# -----------------------------------------------------------------------------
# It is assumed that the incoming argument will always be a single letter string
def check_vowel_or_consonant(letter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if letter in vowels:
        result = "vowel"
    else:
        result = "consonant"

    return result


def choose_cons():
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
                  'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    return random.choice(consonants)


def choose_vowel():
    vowels = ['a', 'e', 'i', 'o', 'u']
    return random.choice(vowels)


def get_choice(opt):
    if opt == "int":
        try:
            choice = int(input())
        except:
            choice = -1
        return choice
    elif opt == "str":
        try:
            choice = str(input())
        except:
            choice = "bad"
        return choice
    else:
        return None


def generate_word():
    new_word = ""
    word_length = random.randrange(3, 14)
    consec_cons_count = 0
    consec_vowel_count = 0

    while len(new_word) <= word_length:
        letter = random.choice(string.ascii_letters)

        if len(new_word) == 0:
            letter = letter.upper()
        else:
            letter = letter.lower()

        vc_check = check_vowel_or_consonant(letter)

        if vc_check == "consonant":
            consec_cons_count += 1
            if consec_cons_count > 1:
                letter = choose_vowel()
                consec_cons_count = 0
            new_word += letter

        elif vc_check == "vowel":
            consec_vowel_count += 1
            if consec_vowel_count > 1:
                letter = choose_cons()
                consec_vowel_count = 0
            new_word += letter

    return new_word
