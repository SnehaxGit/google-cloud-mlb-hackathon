# src/fetch_mlb_data.py

import requests
import json
from config import GUMBO_API_URL

def fetch_live_game_data(game_pk):
    """Fetch live game data from MLB Stats API."""
    url = GUMBO_API_URL.format(game_pk=game_pk)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game data: {e}")
        return None

if __name__ == "__main__":
    game_pk = "716463"  # Example game ID (you can dynamically fetch this)
    data = fetch_live_game_data(game_pk)
    if data:
        with open("data/game_data.json", "w") as f:
            json.dump(data, f, indent=4)
