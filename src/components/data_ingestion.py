import os

from src.data_access.shelf_genie_data import ShelfGenieDataCollection
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.logger import logging
from src.constants import *

class DataIngestion:
    def data_ingestion_initialize(self) -> DataIngestionArtifact:
        '''
        This method start the data ingestion part
        '''
        data_collection: ShelfGenieDataCollection = ShelfGenieDataCollection(
            db_name=DB_NAME,
            collection_name=COLLECTION_NAME,
            connection_url=os.getenv(CONNECTION_URL)
        )
        data_ingestion_config: DataIngestionConfig = DataIngestionConfig() # defining the DataIngestionConfig class
        
        data = data_collection.data_collection(data_ingestion_config.feature_store_folder_path)
        data_cleaning = data_collection.data_clean_and_export_to_csv(data, data_ingestion_config.ingested_folder)
        
        data_ingestion_artifact = DataIngestionArtifact(
            ingested_file_path=data_cleaning # saving the file path on DataIngestionArtifact
        )
        logging.info('Data Ingestion Complete...')
        print(data_ingestion_artifact)
        
        return data_ingestion_artifact # returning the data_ingestion_artifact
        
    
    
            
            