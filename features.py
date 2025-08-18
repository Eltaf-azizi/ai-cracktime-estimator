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


LEET_SUBS = {
    'a': '4@', 'e': '3', 'i': '1!', 'o': '0', 's': '5$', 't': '7'
}


def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    counts = Counter(s)
    n = len(s)
    return -sum((c/n) * math.log2(c/n) for c in counts.values())


def charset_size(s: str) -> int:
    sets = [
        any(c in LOWER for c in s),
        any(c in UPPER for c in s),
        any(c in DIGIT for c in s),
        any(c in SYMS for c in s),
    ]
    return 26*sets[0] + 26*sets[1] + 10*sets[2] + 33*sets[3]



def _count_sequences(s: str, rows) -> int:
    c = 0
    sL = s.lower()
    for i in range(len(sL)-2):
        chunk = sL[i:i+3]
        for row in rows:
            if chunk in row or chunk in row[::-1]:
                c += 1
                break
    return c



def keyboard_walks(s: str) -> int:
    return _count_sequences(s, QWERTY_ROWS)



def repeated_runs(s: str) -> int:
    # aaa, 1111, !!!!
    return len(re.findall(r'(.)\1{2,}', s))



def date_like(s: str) -> int:
    # common patterns: 1999, 2012, 12/05, 05-12
    pats = [r'19\d{2}', r'20\d{2}', r'\b\d{2}[/-]\d{2}\b']
    return sum(len(re.findall(p, s)) for p in pats)



def leetiness(s: str) -> int:
    sL = s.lower()
    return sum(any(ch in LEET_SUBS.get(k, '') for ch in sL) for k in LEET_SUBS)


