import sys
import pandas as pd
import numpy as np
import pymongo as pm
import csv
import os
from pathlib import Path
from from_root import from_root

from src.constants import *
from src.logger import logging
from src.exception import MyException
from src.utils.main_utils import load_yaml_file


class ShelfGenieDataCollection:
    
    def __init__(self, db_name: str, collection_name: str, connection_url: str) -> None:
        '''
        This method stablish the connection between database.
        
        :args     :       DB_Name(MongoDB Database Name)
        :args     :       Collection_Name(MongoDB Collection Name)
        :args     :       Connection_URL(MongoDB Connection URL)
        '''
        try:
            logging.info('Data Ingestion Started....')
            self.client = pm.MongoClient(connection_url)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
            logging.info('MongoDB Connected successfully...')
            
        except Exception as e:
            raise MyException(e, sys) from e
        
    def data_collection(self, feature_storage_path: Path) -> Path:
        '''
        This method collects data from MOngoDB and export the clean data in csv format and returns the saved file path.
        
        :args       :       feature_store_file_path( desired file path for saving data )
        '''
        try:
            print('Fetching Data from MongoDB...')
            documents = self.collection.find({})
            first_document = documents[0]
            field_names = list(first_document.keys())
            
            path = Path(feature_storage_path)
            path.mkdir(parents=True, exist_ok=True) # Creating parent folder 
            
            file_path: Path = Path(os.path.join(path,FEATURE_STORE_FILE_NAME))
            file_path.parent.mkdir(parents=True,exist_ok=True) # Creating folder inside parent folder
            
            with open(file_path, 'w', newline='') as csvfile: # Saving the file inside the desired folder

                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                for document in documents:
                    writer.writerow(document)
                    
            logging.info('Data Ingestion Successfull...')
            return file_path # returning the saved file path for data cleaning.
            
        except Exception as e:
            raise MyException(e, sys) from e
        
    
    def data_clean_and_export_to_csv(self, feature_store_file_path: Path, ingested_file_path: Path) -> Path:
        '''
        This method remove all the unnecessary columns and export the clean data in csv format and returns the saved file path.
        
        :args       :       feature_store_file_path( file path that data_collection method returns)
        :args       :       ingested_file_path( desired file path for saving clean data )
        '''
        try:
            logging.info('Removing Unnecessary Columns.')
            
            schema = load_yaml_file(os.path.join(from_root(),'config', 'schema.yaml')) # loading schema.yaml file to remove unnecessary columns.
            data: pd.DataFrame = pd.read_csv(feature_store_file_path, encoding='latin-1') # loading the raw csv file and turning into a dataframe.
            if schema['drop_column']:
                data.rename(columns={'Unnamed: 0' : 'Unnamed'}, inplace=True) # renaming the column.
                clean_data = data.drop(schema['drop_column'], axis=1) # droping unnecessary columns.
                
            clean_data_file_path = Path(os.path.join(ingested_file_path, INGESTED_FILE_NAME))
            clean_data_file_path.parent.mkdir(parents=True, exist_ok=True) # creating folder inside the parent folder.
            clean_data.to_csv(clean_data_file_path) # saving that on desired folder in csv format.
            logging.info('Successfully Removed Unnecessary Columns.')
            return clean_data_file_path # returning saved file path for artifact.
        
        except Exception as e:
            raise MyException(e, sys) from e