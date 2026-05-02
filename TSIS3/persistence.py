import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

DEFAULT_SETTINGS = {
    "sound": False,
    "car_color": [50, 100, 220],
    "difficulty": "normal"
}


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []


def save_leaderboard(scores):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def add_score(name, score, distance, coins):
    scores = load_leaderboard()
    scores.append({"name": name, "score": score, "distance": distance, "coins": coins})
    scores.sort(key=lambda x: x["score"], reverse=True)
    scores = scores[:10]
    save_leaderboard(scores)
