import random, string, math
import pandas as pd
from pathlib import Path
from features import extract_features


random.seed(42)


# Load dictionary
COMMON_WORDS = set()
with open("common_words.txt", "r", encoding="utf-8") as f:
    for line in f:
        w = line.strip()
        if w:
            COMMON_WORDS.add(w)


ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}?,." # modest symbol set



def rand_digits(n):
    return "".join(random.choice(string.digits) for _ in range(n))




def rand_mix(n):
    return "".join(random.choice(ALPHABET) for _ in range(n))




def rand_word():
    return random.choice(list(COMMON_WORDS))




def gen_password():
    patterns = [
        "word+year", "CapWord+digits", "word123", "Word!digits",
        "random16", "leetWord", "digitsOnly", "mix8to12"
    ]

