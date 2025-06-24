from dataclasses import dataclass
from from_root import from_root
from datetime import datetime
import os
from src.constants import *

@dataclass
class DataIngestionConfig:
    artefact_folder_path: str = os.path.join(from_root(),ARTEFACT_DIR)
    timestamp_folder_path: str = os.path.join(artefact_folder_path, TIMESTAMP)
    data_ingestion_folder_path: str = os.path.join(timestamp_folder_path, DATA_INGESTION_FOLDER_NAME)
    feature_store_folder_path: str = os.path.join(data_ingestion_folder_path, FEATURE_STORE_FOLDER_NAME)
    ingested_folder: str = os.path.join(data_ingestion_folder_path, INGESTED_FOLDER_NAME)
    
    