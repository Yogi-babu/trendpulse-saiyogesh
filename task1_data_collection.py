import requests
import json
import os
import time
from datetime import datetime

BASE_URL = "https://hacker-news.firebaseio.com/v0"
LIMIT = 500

# Category keywords mapping
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# ---------------- FETCH IDS ----------------
def get_story_ids():
    res = requests.get(f"{BASE_URL}/topstories.json")
    return res.json()[:LIMIT]

# ---------------- FETCH STORY ----------------
def get_story(id):
    try:
        res = requests.get(
            f"{BASE_URL}/item/{id}.json",
            headers={"User-Agent": "TrendPulse/1.0"}
        )
        return res.json()
    except:
        print(f"Error fetching {id}")
        return None

# ---------------- CATEGORY ----------------
def categorize(title):
    title = title.lower()

    for category, words in CATEGORIES.items():
        for word in words:
            if word in title:
                return category

    return None

# ---------------- EXTRACT ----------------
def extract(story):
    return {
        "post_id": story.get("id"),
        "title": story.get("title", "No Title"),
        "category": categorize(story.get("title", "")),
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", "Unknown"),
        "collected_at": datetime.now().isoformat()
    }

# ---------------- SAVE ----------------
def save(data):
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Collected {len(data)} stories. Saved to {filename}")

# ---------------- MAIN ----------------
def main():
    print("Fetching data...")

    ids = get_story_ids()

    results = []
    count = {cat: 0 for cat in CATEGORIES}

    for id in ids:
        story = get_story(id)

        if not story or "title" not in story:
            continue

        category = categorize(story["title"])
        if not category:
            continue

        if count[category] < 25:
            results.append(extract(story))
            count[category] += 1

        # stop early when done
        if all(c >= 25 for c in count.values()):
            break

    save(results)

# run
if __name__ == "__main__":
    main()