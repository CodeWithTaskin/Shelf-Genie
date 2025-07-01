import os
import sys
import numpy as np
import pandas as pd

from pathlib import Path
from src.constants import *
from src.logging import logging
from src.exception import MyException
from src.azure.storage.azure_storage import AzureBlobStorage
from src.entity.config_entity import RecommendationEngineConfig
from src.utils.main_utils import zipper, convert_and_load_pkl_file


class RecommendationEngine:
    def __init__(self):
        try:
            self.recommendation_engine_config : RecommendationEngineConfig = RecommendationEngineConfig()
            self.azure_blob_storage : AzureBlobStorage = AzureBlobStorage()
            
            requirements_folder_path = self.recommendation_engine_config.required_file_path
            os.makedirs(requirements_folder_path, exist_ok=True)
            
            download_file = os.path.join(requirements_folder_path, ZIP_FILE_NAME)
            
            logging.info('Checking file exist or not....')
            is_file_exist = self.azure_blob_storage.is_exist(
                blob_file_name=ZIP_FILE_NAME,
                container_name=AZURE_CONTAINER_NAME
            )
            
            if is_file_exist == True:
                try:
                    logging.info('Downloading file from Azure Blob....')
                    self.azure_blob_storage.download(
                        blob_file_name=ZIP_FILE_NAME,
                        download_file_path=download_file
                    )
                    logging.info('Successfully Downloaded....')
                    
                    logging.info('Unpacking zip file....')
                    zipper(
                        output_folder_name=requirements_folder_path,
                        source_folder_path=download_file,
                        statement='unpack'
                    )
                    logging.info('Successfully Unpacked....')
                    
                except Exception as e:
                    raise MyException(e, sys) from e
            else:
                logging.info('file in not present....')
                
        except Exception as e:
            raise MyException(e, sys) from e


    def recommend_name(self,book_name):
        recommended_books = []
        pt_df = convert_and_load_pkl_file(
            file_path=os.path.join(self.recommendation_engine_config.required_file_path, TRANSFORMED_FILE_NAME), statement='load'
        )
        similarity = convert_and_load_pkl_file(
            file_path=os.path.join(self.recommendation_engine_config.required_file_path, MODEL_FILE_NAME), statement='load'
        )
        index = np.where(pt_df.index == book_name)[0][0]
        distance = sorted(list(enumerate(similarity[index])), key=lambda x:x[1], reverse=True)[1:6]
        for i in distance:
            recommended_books.append(pt_df.index[i[0]])
        return recommended_books
    
    def recommendation(self,book_name):
        recommended_books_name_list = self.recommend_name(book_name=book_name)
        recommended_books = []
        df = pd.read_csv(os.path.join(self.recommendation_engine_config.required_file_path, INGESTED_FILE_NAME))
        for name in recommended_books_name_list:
            filtering_by_book_name = df[df['Book-Title'] == name]
            removing_dublicates = filtering_by_book_name.drop_duplicates('ISBN')
            picking_the_best_book = removing_dublicates.sort_values(['num_of_reating' and 'Book-Rating' and 'avg_of_reating'], ascending=False).head(1).to_dict(orient='records')
            recommended_books.append(picking_the_best_book[0])
        converting_into_dataframe = pd.DataFrame(recommended_books)
        
        recommended_books_in_json = converting_into_dataframe.to_json(orient='index')
        return recommended_books_in_json
    
    def top_books(self):
        top_books = convert_and_load_pkl_file(
            file_path=os.path.join(self.recommendation_engine_config.required_file_path, TRANSFORMED_DF_FILE_NAME), statement='load'
        )
        top_books_in_json = top_books.to_json(orient='index')
        return top_books_in_json