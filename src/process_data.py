# src/process_data.py

import json
import pandas as pd

def load_game_data(file_path):
    """Load and parse game data from a JSON file."""
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def extract_player_stats(game_data):
    """Extract player stats from game data."""
    players = []
    for inning in game_data.get('liveData', {}).get('plays', {}).get('allPlays', []):
        for player in inning.get('players', []):
            player_info = player.get('player')
            if player_info:
                players.append({
                    'player_id': player_info.get('id'),
                    'player_name': player_info.get('fullName'),
                    'team': player_info.get('team', {}).get('name'),
                    'position': player_info.get('position', {}).get('abbreviation'),
                })
    return pd.DataFrame(players)

if __name__ == "__main__":
    data = load_game_data("data/game_data.json")
    player_stats = extract_player_stats(data)
    player_stats.to_csv("data/player_stats.csv", index=False)
    print("Player stats extracted and saved to 'data/player_stats.csv'")
