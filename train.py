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


if __name__ == "__main__":
    df = pd.read_csv("train_offline.csv")
    X = df[FEATURES]
    y = df["log10_seconds"]


    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)


    pred = model.predict(X_val)
    mae = mean_absolute_error(y_val, pred)
    r2 = r2_score(y_val, pred)
    print("MAE (log10 seconds):", round(mae, 3), "R2:", round(r2, 3))


    joblib.dump(model, "model_offline.joblib")
    print("Saved model_offline.joblib")

    