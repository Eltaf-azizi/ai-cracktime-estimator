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