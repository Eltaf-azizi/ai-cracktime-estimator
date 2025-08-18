import math, re, string
from collections import Counter

LOWER = set(string.ascii_lowercase)
UPPER = set(string.ascii_uppercase)
DIGIT = set(string.digits)
SYMS  = set(string.punctuation)

# Rows to detect simple keyboard walks like "qwe", "asd", "123"
QWERTY_ROWS = [
    "1234567890",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]
