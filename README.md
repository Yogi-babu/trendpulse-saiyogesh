# 📊 TrendPulse — Task 1: Fetch Data from API

## 🚀 Project Overview

TrendPulse is a data pipeline project where trending stories are fetched from Hacker News API, sorted, and stored as structured JSON.

This repository hosts **Task 1 – Data Collection**.

---

## 📌 Features

* Retrieves 500 top stories from Hacker News API
* Extracts needed information
* Sorts articles into categories:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Deals with API exceptions
* Outputs to JSON

---

## 🛠️ Tech Stack

* Python
* requests
* JSON

---

## 📂 Directory Structure

trendpulse/
│
├── data/
│   ├── trends_20260414.json
│   └── trends_cleaned_20260414.csv
│
├── src/
│   ├── task1_data_collection.py
│   ├── task2_clean_csv.py
│   ├── task3_analysis.py
│   └── task4_visualization.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py   (optional but impressive ⭐)

---

## ⚙️ Process Outline

### Step 1: Retrieving Stories

Endpoint: 
https://hacker-news.firebaseio.com/v0/topstories.json

### Step 2: Fetching Story Information

Endpoint:
https://hacker-news.firebaseio.com/v0/item/{id}.json

### Step 3: Story Classification

Stories are classified into:

| Category      | Keywords                       |
| ------------- | ------------------------------ |
| Technology    | Artificial Intelligence, APIs, software |
| World News    | politics, government, election   |
| Sports        | NFL, FIFA, NBA                 |
| Science       | research, NASA, physics         |
| Entertainment | Netflix, movies, music          |

---

## ▶️ Running The Script

### 1. Installing Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Launching The Script

```bash
python task1_data_collection.py
```

---

## 📦 Output

* JSON File Created:

```
data/trends_YYYYMMDD.json
```

* Containing:

  * At least 100 stories
  * No more than 25 per category

---

## 🧾 Collected Information

| Field        | Description        |
| ------------ | ------------------ |
| post_id      | Story ID           |
| title        | Title              |
| category     | Story Category     |
| score        | Upvote             |
| num_comments | Comments count     |
| author       | Author Username    |
| collected_at | Timestamp         |

---

## ✅ Submission Checklist

* [x] Python script running smoothly
* [x] JSON file saved to `data/` directory
* [x] Minimum 100 stories collected
* [x] All fields listed above collected
* [x] Commented properly

---

## ⚠️ Additional Notes

* Script has delay for not to overload API
* Exceptions dealt with elegantly
* Good code practice is observed

---

## 👨‍💻 Developer Info

Sai Yogesh

GitHub: <https://github.com/<yogi-babu>>
