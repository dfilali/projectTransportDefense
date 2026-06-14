import sys
import os
import pytest
import pandas as pd
import numpy as np

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from src.data_processing.process_transport_data import determine_status_from_message
from src.models.traffic_prediction import TrafficPredictor

def test_determine_status_from_message():
    # Test critical status keywords
    assert determine_status_from_message("Le service est interrompu sur l'ensemble de la ligne.") == "critical"
    assert determine_status_from_message("La station est fermée pour travaux.") == "critical"
    
    # Test major status keywords
    assert determine_status_from_message("Trafic très perturbé en raison d'un incident technique.") == "major"
    assert determine_status_from_message("Ralentissement important sur la ligne.") == "major"
    
    # Test minor status keywords
    assert determine_status_from_message("Retard de 10 minutes à prévoir.") == "minor"
    assert determine_status_from_message("Léger retard à prévoir.") == "minor"
    
    # Test normal status keywords
    assert determine_status_from_message("Le trafic est normal sur toute la ligne.") == "normal"
    assert determine_status_from_message("Reprise progressive du trafic.") == "normal"
    
    # Test defaults
    assert determine_status_from_message("") == "unknown"
    assert determine_status_from_message("Message quelconque sans mots clés spécifiques.") == "normal"

def test_traffic_predictor_prediction():
    # Test mock prediction with the trained model
    predictor = TrafficPredictor()
    model_path = os.path.join(root_dir, "src", "models", "traffic_model.joblib")
    
    if os.path.exists(model_path):
        predictor.load_model(model_path)
        
        weather_forecast = {
            "temperature": 20.0,
            "humidity": 60.0,
            "precipitation": 0.0,
            "wind_speed": 10.0
        }
        
        # Predict congestion for 8 AM on a Monday (day 0)
        prediction = predictor.predict(weather_forecast, hour=8, day_of_week=0)
        
        assert isinstance(prediction, (int, float, np.float64, np.float32))
        assert 0.0 <= prediction <= 5.0
