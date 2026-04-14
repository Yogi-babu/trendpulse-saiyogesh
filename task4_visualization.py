import pandas as pd
import matplotlib.pyplot as plt
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

    return pd.read_csv(filepath)


# ================= PLOTS =================

def plot_category_distribution(df):
    """Bar chart: number of stories per category"""
    counts = df["category"].value_counts()

    counts.plot(kind="bar")
    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.show()


def plot_avg_score(df):
    """Bar chart: average score per category"""
    avg_score = df.groupby("category")["score"].mean()

    avg_score.plot(kind="bar")
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.show()


def plot_avg_comments(df):
    """Bar chart: average comments per category"""
    avg_comments = df.groupby("category")["num_comments"].mean()

    avg_comments.plot(kind="bar")
    plt.title("Average Comments per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Comments")
    plt.show()


# ================= MAIN =================

def main():
    df = load_csv()

    if df is None:
        return

    plot_category_distribution(df)
    plot_avg_score(df)
    plot_avg_comments(df)


if __name__ == "__main__":
    main()