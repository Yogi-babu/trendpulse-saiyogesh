import pandas as pd
import numpy as np
import os

# ================= LOAD CSV =================

def load_csv():
    folder = "data"

    files = [f for f in os.listdir(folder) if f.startswith("trends_cleaned_") and f.endswith(".csv")]

    if not files:
        print("No cleaned CSV found!")
        return None

    latest_file = sorted(files)[-1]
    filepath = os.path.join(folder, latest_file)

    print(f"Loading: {filepath}")

    df = pd.read_csv(filepath)
    return df


# ================= ANALYSIS =================

def analyze(df):

    print("\n===== BASIC INFO =====")
    print("Total stories:", len(df))

    print("\n===== STORIES PER CATEGORY =====")
    print(df["category"].value_counts())

    print("\n===== AVERAGE SCORE PER CATEGORY =====")
    print(df.groupby("category")["score"].mean().round(2))

    print("\n===== AVERAGE COMMENTS PER CATEGORY =====")
    print(df.groupby("category")["num_comments"].mean().round(2))

    print("\n===== TOP 5 STORIES (BY SCORE) =====")
    print(df.sort_values(by="score", ascending=False)[["title", "score"]].head(5))

    print("\n===== MOST ACTIVE AUTHORS =====")
    print(df["author"].value_counts().head(5))

    best_category = df.groupby("category")["score"].mean().idxmax()
    print("Best performing category:", best_category)

    engagement = df.groupby("category")["num_comments"].mean().idxmax()
    print("Most engaging category:", engagement)

    viral = df[(df["score"] > 200) & (df["num_comments"] > 100)]
    print("\nViral Stories:\n", viral[["title", "score", "num_comments"]].head())

    top_authors = df.groupby("author")["score"].sum().sort_values(ascending=False).head(5)
    print("\nTop Influential Authors:\n", top_authors)

    correlation = df["score"].corr(df["num_comments"])
    print("\nScore vs Comments Correlation:", round(correlation, 2))


# ================= NUMPY BONUS =================

def numpy_analysis(df):
    print("\n===== NUMPY INSIGHTS =====")

    scores = df["score"].values
    comments = df["num_comments"].values

    print("Max score:", np.max(scores))
    print("Min score:", np.min(scores))
    print("Average score:", np.mean(scores).round(2))

    print("Max comments:", np.max(comments))
    print("Average comments:", np.mean(comments).round(2))


# ================= MAIN =================

def main():
    df = load_csv()

    if df is None:
        return

    analyze(df)
    numpy_analysis(df)


if __name__ == "__main__":
    main()
    
