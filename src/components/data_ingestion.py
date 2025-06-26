import os
import sys
import csv
import pandas as pd
import numpy as np
import pymongo as pm

from pathlib import Path
from from_root import from_root

from src.constants import *
from src.logging import logging
from src.exception import MyException
from src.utils.main_utils import load_yaml_file
from src.entity.artifact_entity import DataIngestionArtifact
from src.configuration.mongodb_connection import MongoDBConnection

class DataIngestion:
    def data_collection(self, feature_storage_path: Path) -> Path:
        try:
            connection : MongoDBConnection = MongoDBConnection(
                db_name=DB_NAME,
                collection_name=COLLECTION_NAME,
                connection_url=os.getenv(CONNECTION_URL)
            )
            
            documents = connection.collection.find({})
            first_document = documents[0]
            field_names = list(first_document.keys())
            file_path : Path = Path(feature_storage_path)
            file_path.parent.mkdir(parents=True,exist_ok=True)
            print('Fetching Data from MongoDB....')
            
            with open(file_path, 'w', newline='') as csvfile: # Saving the file inside the desired folder
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                for document in documents:
                    writer.writerow(document)
                    
            return file_path
        
        except Exception as e:
            raise MyException(e, sys) from e
    
    def data_cleaning_and_export_to_csv(self, feature_storage_path: Path, ingested_path: Path) -> Path:
        try:
            feature_store_file_path : Path = self.data_collection(
                feature_storage_path=feature_storage_path
            )
            schema = load_yaml_file(os.path.join(from_root(),'config', 'schema.yaml'))
            df: pd.DataFrame = pd.read_csv(feature_store_file_path, encoding='latin-1')
            
            if schema['drop_column']:
                clean_data = df.drop(schema['drop_column'], axis=1) # droping unnecessary columns.
            
            clean_data_file_path: Path = Path(ingested_path)
            clean_data_file_path.parent.mkdir(parents=True,exist_ok=True)# creating folder inside the parent folder.
            
            clean_data.to_csv(clean_data_file_path) # saving that on desired folder in csv format.
            logging.info('Successfully Removed Unnecessary Columns.')
            
            return clean_data_file_path
        
        except Exception as e:
            raise MyException(e, sys) from e
        
    def data_ingestion_initialize(self,  feature_storage_path: Path, ingested_path: Path) -> DataIngestionArtifact:
        try:
            ingested_file_path : Path = self.data_cleaning_and_export_to_csv(
                feature_storage_path=feature_storage_path,
                ingested_path=ingested_path
            )
            
            data_ingestion_artifact : DataIngestionArtifact = DataIngestionArtifact(
                ingested_file_path=ingested_file_path
            )
            print(data_ingestion_artifact)
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e