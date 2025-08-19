import math, joblib
from features import extract_features


# Load small dictionary for features
COMMON_WORDS = set()
with open("common_words.txt", "r", encoding="utf-8") as f:
    for line in f:
        w = line.strip()
        if w:
            COMMON_WORDS.add(w)


FEATURES = [
    "len", "charset_size", "entropy",
    "has_lower", "has_upper", "has_digit", "has_symbol",
    "keyboard_walks", "repeated_runs", "date_like", "leetiness",
    "unique_chars", "starts_with_cap", "ends_with_digit", "dict_hits",
    "unique_ratio", "entropy_per_char"
]