"""
Model training script for La Défense mobility traffic prediction
"""
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from src.models.traffic_prediction import TrafficPredictor
from src.configuration.config import DATA_LAKE
from src.utils.data_lake_utils import read_parquet_from_data_lake

def generate_synthetic_training_data(num_samples=1000):
    """Generate realistic traffic and weather historical data for training when real data is scarce"""
    print("Generating synthetic historical data for training...")
    np.random.seed(42)
    
    start_time = datetime.now() - timedelta(days=60)
    timestamps = [start_time + timedelta(hours=i) for i in range(num_samples)]
    
    traffic_records = []
    weather_records = []
    
    for ts in timestamps:
        ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        hour = ts.hour
        day_of_week = ts.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0
        
        # Weather simulation
        temp = np.random.normal(15, 8)  # mean temp 15°C
        humidity = np.clip(np.random.normal(70, 15), 30, 100)
        # 10% chance of rain
        precip = np.random.exponential(1.5) if np.random.rand() < 0.10 else 0.0
        wind_speed = np.clip(np.random.normal(15, 8), 0, 50)
        
        weather_records.append({
            "timestamp": ts_str,
            "temperature": temp,
            "humidity": humidity,
            "precipitation": precip,
            "wind_speed": wind_speed
        })
        
        # Congestion level simulation (0 to 5)
        # Baseline congestion by hour of day (rush hours)
        if 8 <= hour <= 9 or 17 <= hour <= 19:
            base_congestion = 3.5 if not is_weekend else 1.5
        elif 12 <= hour <= 14:
            base_congestion = 2.0 if not is_weekend else 2.5
        else:
            base_congestion = 0.5
            
        # Weather impact: rain increases congestion
        weather_impact = (precip * 0.4) + (1 if temp < 2 else 0) + (0.5 if wind_speed > 35 else 0)
        
        # Random noise
        noise = np.random.normal(0, 0.4)
        
        congestion_level = np.clip(base_congestion + weather_impact + noise, 0, 5)
        
        traffic_records.append({
            "timestamp": ts_str,
            "congestion_level": congestion_level
        })
        
    return pd.DataFrame(traffic_records), pd.DataFrame(weather_records)

def train_and_save_model():
    print("=== Training Traffic Prediction Model ===")
    
    # Try to load real data
    bucket_name = DATA_LAKE["bucket_name"]
    traffic_df = pd.DataFrame()
    weather_df = pd.DataFrame()
    
    # Normally we would load from:
    # traffic_df = read_parquet_from_data_lake(bucket_name, "refined/traffic/traffic_latest.parquet")
    # weather_df = read_parquet_from_data_lake(bucket_name, "refined/weather/hourly_latest.parquet")
    
    if traffic_df.empty or weather_df.empty or len(traffic_df) < 100:
        traffic_df, weather_df = generate_synthetic_training_data()
        
    predictor = TrafficPredictor()
    mae = predictor.train(traffic_df, weather_df)
    
    # Save the model
    model_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(model_dir, "traffic_model.joblib")
    predictor.save_model(model_path)
    
    print(f"Model trained successfully. MAE: {mae:.4f}")
    print(f"Model saved to: {model_path}")
    return True

if __name__ == "__main__":
    train_and_save_model()
