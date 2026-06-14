"""
Automated extraction scheduler for La Défense mobility data lake
This script orchestrates all data extraction and processing tasks
"""
import schedule
import time
import os
import sys
from datetime import datetime
import argparse

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from src.configuration.config import EXTRACTION_CONFIG

# Import extraction functions
from src.data_extraction.extract_transport import extract_ratp_transport_data
from src.data_extraction.extract_idfm_data import extract_idfm_data
from src.data_extraction.extract_visual_crossing_weather import extract_visual_crossing_data
from src.data_extraction.extract_traffic import extract_traffic_data
from src.data_extraction.extract_ratp_stations import extract_ratp_station_data
from src.data_extraction.extract_osm_stations import extract_osm_station_data

# Import processing functions
from src.data_processing.process_transport_data import process_transport_data
from src.data_processing.process_idfm_data import process_idfm_data
from src.data_processing.process_weather_data import process_weather_data
from src.data_processing.process_stations_data import process_combined_station_data
from src.data_processing.data_quality import run_basic_checks


def run_transport_extraction():
    """Run transport data extraction and processing"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running transport data extraction...")
    extract_ratp_transport_data()
    process_transport_data()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transport data extraction complete")

def run_weather_extraction():
    """Run weather data extraction and processing"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running weather data extraction...")
    extract_visual_crossing_data()
    process_weather_data()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Weather data extraction complete")

def run_traffic_extraction():
    """Run traffic data extraction"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running traffic data extraction...")
    extract_traffic_data()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Traffic data extraction complete")

def run_quality_check():
    """Run basic data quality checks"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running data quality checks...")
    run_basic_checks()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Data quality checks complete")

def run_station_extraction():
    """Run station data extraction and processing"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running station data extraction...")
    extract_ratp_station_data()
    extract_osm_station_data()
    process_combined_station_data()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Station data extraction complete")

def run_idfm_extraction():
    """Run IDFM data extraction and processing"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running IDFM data extraction...")
    extract_idfm_data()
    process_idfm_data()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] IDFM data extraction complete")

def run_all_extractions():
    """Run all data extraction processes"""
    print(f"\n--- Starting complete extraction at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    run_transport_extraction()
    run_idfm_extraction()
    run_weather_extraction()
    run_traffic_extraction()
    run_station_extraction()
    run_quality_check()

    print(f"\n--- Completed extraction at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

def setup_schedule():
    """Set up the extraction schedule based on configuration"""
    # Get frequencies from configuration
    transport_freq = EXTRACTION_CONFIG["transport"]["frequency_minutes"]
    weather_freq = EXTRACTION_CONFIG["weather"]["frequency_minutes"]
    traffic_freq = EXTRACTION_CONFIG["traffic"]["frequency_minutes"]
    stations_freq = EXTRACTION_CONFIG["stations"]["frequency_minutes"]
    dataquality_freq = EXTRACTION_CONFIG["dataQuality"]["frequency_minutes"]

    # Schedule transport extraction
    schedule.every(transport_freq).minutes.do(run_transport_extraction)

    # Schedule IDFM extraction
    schedule.every(transport_freq).minutes.do(run_idfm_extraction)

    # Schedule weather extraction
    schedule.every(weather_freq).minutes.do(run_weather_extraction)

    # Schedule traffic extraction
    schedule.every(traffic_freq).minutes.do(run_traffic_extraction)

    # Schedule station extraction (typically once per day)
    schedule.every(stations_freq).minutes.do(run_station_extraction)

    # Schedule data quality checks
    schedule.every(dataquality_freq).minutes.do(run_quality_check)

    print("Extraction schedule configured:")
    print(f"- Transport data: every {transport_freq} minutes")
    print(f"- IDFM data: every {transport_freq} minutes")
    print(f"- Weather data: every {weather_freq} minutes")
    print(f"- Traffic data: every {traffic_freq} minutes")
    print(f"- Station data: every {stations_freq} minutes")
    print(f"- Data quality: every {dataquality_freq} minutes")
    print("\nPress Ctrl+C to stop the scheduler.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='La Défense Mobility Data Extraction')
    parser.add_argument('--schedule', action='store_true', help='Run as a scheduled service')
    parser.add_argument('--extract', choices=['all', 'transport', 'idfm', 'weather', 'traffic', 'stations', 'quality'],
                        help='Run a specific extraction')

    args = parser.parse_args()

    if args.schedule:
        # Run all extractions immediately on startup
        run_all_extractions()

        # Set up scheduled runs
        setup_schedule()

        # Run the scheduler
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nScheduler stopped by user.")

    elif args.extract:
        if args.extract == 'all':
            run_all_extractions()
        elif args.extract == 'transport':
            run_transport_extraction()
        elif args.extract == 'idfm':
            run_idfm_extraction()
        elif args.extract == 'weather':
            run_weather_extraction()
        elif args.extract == 'traffic':
            run_traffic_extraction()
        elif args.extract == 'stations':
            run_station_extraction()
        elif args.extract == 'quality':
            run_quality_check()

    else:
        # By default, run all extractions once
        run_all_extractions()