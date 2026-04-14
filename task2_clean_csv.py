import pandas as pd
import json
import os
from datetime import datetime

# ================= LOAD JSON =================

def load_json():
    """Load latest JSON file from data folder"""
    folder = "data"

    files = [f for f in os.listdir(folder) if f.startswith("trends_") and f.endswith(".json")]

    if not files:
        print("No JSON file found!")
        return None

    # get latest file
    latest_file = sorted(files)[-1]
    filepath = os.path.join(folder, latest_file)

    print(f"Loading file: {filepath}")

    with open(filepath, "r") as f:
        data = json.load(f)

    return data


# ================= CLEAN DATA =================

def clean_data(data):
    """Convert JSON to DataFrame and clean it"""

    df = pd.DataFrame(data)

    print("\nInitial shape:", df.shape)

    # Remove duplicates
    df = df.drop_duplicates(subset=["post_id"])

    # Remove rows with missing title
    df = df.dropna(subset=["title"])

    # Convert types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Convert datetime
    df["collected_at"] = pd.to_datetime(df["collected_at"])

    # Sort by score (highest first)
    df = df.sort_values(by="score", ascending=False)

    print("Cleaned shape:", df.shape)

    return df


# ================= SAVE CSV =================

def save_csv(df):
    """Save cleaned data into CSV"""

    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_cleaned_{datetime.now().strftime('%Y%m%d')}.csv"

    df.to_csv(filename, index=False)

    print(f"\nSaved cleaned CSV to {filename}")


# ================= MAIN =================

def main():
    data = load_json()

    if not data:
        return

    df = clean_data(data)

    save_csv(df)


if __name__ == "__main__":
    main()