import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from src.utils.logger import get_logger

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

logger = get_logger()

class MainPipeline:
    def __init__(self):
        logger.info("Pipeline initialized")

    def run(self):
        logger.info("Step 1 - Data Extraction")
        try:
            extract_ratp_transport_data()
            extract_idfm_data()
            extract_visual_crossing_data()
            extract_traffic_data()
            extract_ratp_station_data()
            extract_osm_station_data()
            logger.info("Data extraction step completed successfully")
        except Exception as e:
            logger.error(f"Error during data extraction: {str(e)}")

        logger.info("Step 2 - Data Processing")
        try:
            process_transport_data()
            process_idfm_data()
            process_weather_data()
            process_combined_station_data()
            logger.info("Data processing step completed successfully")
        except Exception as e:
            logger.error(f"Error during data processing: {str(e)}")

        logger.info("Step 3 - Data Quality Checks")
        try:
            run_basic_checks()
            logger.info("Data quality checks completed successfully")
        except Exception as e:
            logger.error(f"Error during data quality checks: {str(e)}")

        logger.info("Pipeline completed")
        return True
