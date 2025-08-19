import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
import joblib


FEATURES = [
    "len", "charset_size", "entropy",
    "has_lower", "has_upper", "has_digit", "has_symbol",
    "keyboard_walks", "repeated_runs", "date_like", "leetiness",
    "unique_chars", "starts_with_cap", "ends_with_digit", "dict_hits",
    "unique_ratio", "entropy_per_char"
]
