# Google Cloud x MLB Hackathon Boilerplate

[Google Cloud x MLB™ Hackathon](https://next2025challenge.devpost.com/)! 

## Directory Structure(To be followed)

```graphql
mlb-fan-engagement-hackathon/
│
├── data/
│   ├── game_data.json           # Example of fetched game data
│
├── notebooks/
│   ├── mlb_game_data_analysis.ipynb  # Jupyter Notebook for analysis & visualization
│
├── src/
│   ├── __init__.py
│   ├── fetch_mlb_data.py        # Code to fetch live game data from the API
│   ├── process_data.py          # Data processing (e.g., extracting stats)
│   ├── ai_integration.py        # Integration with Google Cloud AI models
│   └── utils.py                 # Helper functions for common tasks
│
├── requirements.txt             # Python dependencies
├── config.py                    # Configuration for API keys and endpoints
└── README.md                    # Project description and setup instructions

```

This is the boilerplate codebase for the **MLB™ Fan Engagement Hackathon**, where you can use Google Cloud's AI tools and MLB's GUMBO data feeds to build innovative fan engagement solutions.

## Getting Started

1. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Fetching Data

You can fetch live game data using the `fetch_mlb_data.py` :  
`python src/fetch_mlb_data.py`

## Data Processing

Once you've fetched the data, you can process it using the `process_data.py` :  
`python src/process_data.py`

## AI Integration

To integrate with Google Cloud AI, you can use the `ai_integration.py` :  
`python src/ai_integration.py`

## Analyzing Data
Use the Jupyter notebook `notebooks/mlb_game_data_analysis.ipynb` to analyze and visualize the data.


### Modify `requirement.text` as follows:

```
requests==2.28.2
pandas==1.5.3
google-cloud==3.0.2
google-cloud-vertex-ai==2.12.0
notebook==6.5.4
```

### Step2: Codebase Steup

#### Configuration File `Config.py`

This file is used to store all the API Keys

#### Code to Fetch Live MLB Game Data `src/fetch_mlb_data.py`

This script fetches live game data from the MLB Stats API (GUMBO data).

#### Data Processing `src/process_data.py`

This file processes the fetched game data, such as extracting specific statistics.

#### Integration with Google Cloud AI Models `src/ai_integration.py`

This script provides an example of how to use Google Cloud Vertex AI (or other AI models) for predictions based on the processed MLB data.

#### Helper Functions `src/utils.py`

This file contains utility functions that may be reused across various modules.

#### Jupyter Notebook for Analysis `notebooks/mlb_game_data_analysis.ipynb`

Create a Jupyter Notebook to visualize and analyze the data you've fetched. You can load the `player_stats.csv` file, process it, and generate visualizations.

