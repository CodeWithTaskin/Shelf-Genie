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

# Data Validation consents starts from VALIDATION_REPORT_FILE variable

VALIDATION_REPORT_FILE: str = 'report.json'
DATA_VALIDATION_REPORT_FOLDER_NAME: str = 'data_validation'

# Data Transformation consents starts from TRANSFORMATION_FILE_NAME variable

TRANSFORMED_DF_FOLDER_NAME: str = 'data'
TRANSFORMED_FOLDER_NAME: str = 'vector'
TRANSFORMED_DF_FILE_NAME: str = 'top_book.pkl'
TRANSFORMED_FILE_NAME: str = 'vectorize.pkl'
TRANSFORMATION_FOLDER_PATH: str = 'data_transformation'

# Model Trainer consents starts from MODEL_TRAINER_FOLDER_PATH variable

MODEL_TRAINER_FOLDER_PATH: str = 'model_trainer'
MODEL_FOLDER_NAME: str = 'model'
MODEL_FILE_NAME: str = 'model.pkl'