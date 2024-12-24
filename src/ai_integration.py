# src/ai_integration.py

from google.cloud import aiplatform
from config import GCP_PROJECT_ID, GCP_MODEL_ID, GCP_REGION

def predict_with_ai_model(input_data):
    """Send data to Google Cloud Vertex AI model for prediction."""
    aiplatform.init(project=GCP_PROJECT_ID, location=GCP_REGION)
    
    # Instantiate a model
    model = aiplatform.Model(GCP_MODEL_ID)
    
    # Use the model for predictions (example of structured input data)
    prediction = model.predict([input_data])
    
    return prediction

if __name__ == "__main__":
    # Example data input (this should be based on the processed stats data)
    input_data = {"player_id": 660271, "team": "Los Angeles Angels"}
    prediction = predict_with_ai_model(input_data)
    print("AI Model Prediction:", prediction)
