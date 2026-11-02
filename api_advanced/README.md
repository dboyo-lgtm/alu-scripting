# API Advanced - Reddit API

This project contains Python scripts designed to interact with the Reddit API without authentication, utilizing pagination, recursion, regex parsing, and proper request headers (`User-Agent`).

## Environment & Requirements
- **OS:** Ubuntu 14.04 LTS
- **Language:** Python 3 (version 3.4.3)
- **Style Guide:** PEP 8
- **Modules used:** `requests`, `re`, `sys`

---

## Files and Tasks

| Filename | Description |
| :--- | :--- |
| `0-subs.py` | Queries the Reddit API and returns the total number of subscribers for a given subreddit. |
| `1-top_ten.py` | Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. |
| `2-recurse.py` | A recursive function that queries the Reddit API and returns a list of all hot article titles. |
| `3-count.py` | A recursive function that parses the titles of all hot articles and prints a sorted count of specific keywords. |

---

## Usage

Make sure your files are executable:
```bash
chmod +x *.py
