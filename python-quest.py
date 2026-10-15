"""Match a visitor's interests with Erin's public portfolio projects."""

import json
import random

PROJECTS = {
    "web": [
        {"title": "Sun & Ski Sports", "detail": "Past UX/UI and CSS page development work from 2020.", "url": "index.html#sun-ski"},
        {"title": "Rogue Pickings", "detail": "A responsive restaurant practice build.", "url": "https://www.smiddycodes.com/Rouge/index.html"},
    ],
    "games": [
        {"title": "Jack Harlow Musical Wordle", "detail": "A music-themed JavaScript word game.", "url": "https://www.smiddycodes.com/Jack-Musical/JackHarlowWordle1.html"},
        {"title": "Tic-Tac-Toe", "detail": "An interactive JavaScript and React game.", "url": "https://www.smiddycodes.com/Tic-Tac-Toe/index.html"},
    ],
    "code": [
        {"title": "Erin's GitHub", "detail": "Explore Erin's repositories and ongoing code projects.", "url": "https://github.com/Tehambuli"},
    ],
}


def recommend(interest: str) -> str:
    """Return one matching project as a JSON string."""
    if interest not in PROJECTS:
        raise ValueError("Choose web, games, or code.")
    return json.dumps(random.choice(PROJECTS[interest]))
