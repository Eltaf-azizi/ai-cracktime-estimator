import math, joblib
from features import extract_features


# Load small dictionary for 

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


MODEL = joblib.load("model_offline.joblib")




def humanize_seconds(s: float):

    if s < 60:
        return f"{int(s)} seconds"
    m = s / 60

    if m < 60:
        return f"{m:.1f} minutes"
    h = m / 60

    if h < 24:
        return f"{h:.1f} hours"
    d = h / 24

    if d < 365:
        return f"{d:.1f} days"
    y = d / 365
    
    if y < 1e3:

        return f"{y:.2f} years"
    return f"{y/1e3:.2f} millennia"





def advice(feats):
    recs = []

    if feats["len"] < 12:
        recs.append("Increase length to 14–16+ characters.")

    if feats["unique_ratio"] < 0.7:
        recs.append("Avoid repeats; add novel characters.")

    if not feats["has_symbol"]:
        recs.append("Add symbols and place them non-adjacently.")
        
    if not feats["has_upper"] or not feats["has_digit"]:
        recs.append("Mix upper/lower")


