# config.py

# API base URL for MLB StatsAPI
MLB_API_BASE_URL = "https://statsapi.mlb.com/api/v1.1"

# Google Cloud settings (set your project and model IDs)
GCP_PROJECT_ID = "your-google-cloud-project-id"
GCP_MODEL_ID = "your-google-cloud-vertex-ai-model-id"
GCP_REGION = "us-central1"

# GUMBO Data Access endpoints
GUMBO_API_URL = f"{MLB_API_BASE_URL}/game/{{game_pk}}/feed/live"
SCHEDULE_API_URL = f"{MLB_API_BASE_URL}/schedule?sportId=1&season=2024&gameType=R"
