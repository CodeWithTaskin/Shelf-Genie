from datetime import datetime


ARTEFACT_DIR: str = 'artefact'
TIMESTAMP: str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
LOG_DIR = 'logs'
LOG_FILE = f'{TIMESTAMP}.log'
MAX_LOG_SIZE = 5 * 1024 * 1024 #5 MB
BACKUP_COUNT = 3 #Number of backup log to keep


# Data Ingestion consents starts form DB_NAMR variable
DB_NAME: str = 'ShelfGenieDB'
COLLECTION_NAME: str = 'ShelfGenie_Data'
CONNECTION_URL: str = 'MONGODB_URL'
DATA_INGESTION_FOLDER_NAME: str = 'data_ingestion'
INGESTED_FOLDER_NAME: str = 'ingested'
INGESTED_FILE_NAME: str = 'clean_data.csv'
FEATURE_STORE_FOLDER_NAME: str = 'feature_store'
FEATURE_STORE_FILE_NAME: str = 'data.csv'

