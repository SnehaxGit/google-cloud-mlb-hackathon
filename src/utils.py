# src/utils.py

def format_game_data_for_display(game_data):
    """Format raw game data for human-readable display."""
    game_info = {
        "game_status": game_data.get("status", {}).get("detailedState"),
        "home_team": game_data.get("teams", {}).get("home", {}).get("team", {}).get("name"),
        "away_team": game_data.get("teams", {}).get("away", {}).get("team", {}).get("name"),
        "current_inning": game_data.get("liveData", {}).get("linescore", {}).get("currentInning"),
        "score": f"{game_data.get('teams', {}).get('home', {}).get('score')} - {game_data.get('teams', {}).get('away', {}).get('score')}",
    }
    return game_info
