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

    p = random.choice(patterns)


    if p == "word+year":
        return rand_word() + str(random.randint(1990, 2025))
    if p == "CapWord+digits":
        return rand_word().capitalize() + rand_digits(random.randint(2, 4))
    if p == "word123":
        return rand_word() + "123"
    if p == "Word!digits":
        return rand_word().capitalize() + random.choice("!@#$") + rand_digits(random.randint(2, 4))
    if p == "random16":
        return rand_mix(16)
    if p == "leetWord":
        w = (rand_word()
            .replace("a", "4").replace("e", "3")
            .replace("i", "1").replace("o", "0").replace("s", "5"))
        return w + random.choice(["!", "", "07"])






# Heuristic guess-order rank proxy (lower rank = earlier guessed)


def approx_guess_rank(pw: str, feats: dict) -> float:
    rank = 1e12 # base difficulty


    # Early-guess patterns
    if feats["dict_hits"] > 0:
        rank = min(rank, 1e6)
    if feats["ends_with_digit"] and feats["dict_hits"] > 0:
        rank = min(rank, 5e6)
    if feats["keyboard_walks"] > 0 or feats["repeated_runs"] > 0:
        rank = min(rank, 2e7)
    if feats["date_like"] > 0:
        rank = min(rank, 3e7)


    # Length/entropy/charset effects
    L = feats["len"]
    rank *= (1.0 + max(0, (L - 8)) * 0.6)
    rank *= (1.0 - min(feats["entropy_per_char"], 4.0) / 10.0)
    rank *= (1.0 + (feats["charset_size"] / 100.0))


    # Clamp
    return max(1e3, min(rank, 1e20))



def label_seconds_from_rank(rank: float, mode="offline"):
    # guesses per second assumptions
    GPS = 1e9 if mode == "offline" else (100 / 3600) # 100 guesses/hour online
    return rank / GPS



def synth_dataset(n=6000, mode="offline"):
    rows = []
    for _ in range(n):
        pw = gen_password()
        feats = extract_features(pw, dictionary=COMMON_WORDS)
        rank = approx_guess_rank(pw, feats)
        secs = label_seconds_from_rank(rank, mode=mode)
        row = {"password": pw, "rank": rank, "seconds": secs, **feats}
        rows.append(row)
    df = pd.DataFrame(rows)
    df["log10_seconds"] = df["seconds"].apply(lambda x: math.log10(max(1.0, x)))
    return df

if __name__ == "__main__":
    out = Path("train_offline.csv")
    df = synth_dataset(n=6000, mode="offline")
    df.to_csv(out, index=False)
    print(f"Wrote {out} with {len(df)} rows")
    print(df.head(5))

