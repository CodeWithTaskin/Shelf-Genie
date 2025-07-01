import os
import sys
import pandas as pd
import numpy as np
import json
import joblib


from pathlib import Path
from src.logging import logging
from src.exception import MyException
from src.utils.main_utils import load_json, convert_and_load_pkl_file
from src.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact, DataIngestionArtifact
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def check_data_validation_report(self, report_file: DataValidationArtifact) -> bool:
        try:
            logging.info('Checking validation report...')
            validation_report: json = load_json(report_file)
            
            if validation_report['status'] != True:
                logging.info(f'Validation report is: {validation_report['message']}')
                return False
            
            else:
                logging.info(f'Validation report is: {validation_report['message']}')
                return True
            
        except Exception as e:
            raise MyException(e, sys) from e

    def load_data_from_artifact(self, ingested_file_path: DataIngestionArtifact) -> pd.DataFrame:
            '''
            Method      :       load_data_from_artifact.
            Description :       This method loads the data from artifact folder.
            :params     :       ingested_file_path( DataIngestionArtifact ingested file path)
            '''
            try:
                data = pd.read_csv(ingested_file_path, encoding='latin-1')
                logging.info('Clean data successfully loaded....')
                return data
            except Exception as e:
                raise MyException(e, sys) from e
    
    def transform_data_into_vectorized_data(self, df: pd.DataFrame) -> joblib:
        try:
            vectorize_data = df.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
            vectorize_data = vectorize_data.fillna(0)
            return vectorize_data
        
        except Exception as e:
            raise MyException(e, sys) from e
    
    def top_books(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            books_that_more_then_250_num_reating = df[df['num_of_reating'] >= 250]
            dropping_duplicates = books_that_more_then_250_num_reating.drop_duplicates(subset='ISBN')
            dropping_duplicates = books_that_more_then_250_num_reating.drop_duplicates(subset='Book-Title')
            top_books = dropping_duplicates.sort_values('avg_of_reating', ascending=False).head(102)
            return top_books
        except Exception as e:
            raise MyException(e, sys) from e
        
    def data_transformation_initialize(self, report_file: DataValidationArtifact, ingested_file_path: DataIngestionArtifact, transformed_df_file_path: DataTransformationConfig, vectorize_file_path: DataTransformationConfig ) -> DataTransformationArtifact:
        try:
            report = self.check_data_validation_report(
                report_file=report_file
            )
            if report == True:
                df: pd.DataFrame = self.load_data_from_artifact(ingested_file_path=ingested_file_path)
                
                logging.info('Vectorizer Started...')
                vectorize_df = self.transform_data_into_vectorized_data(
                    df=df
                )
                logging.info('Successfully Vectorized....')
                
                logging.info('top books df to pkl started....')
                df_pkl_file_path: Path = Path(transformed_df_file_path)
                df_pkl_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                top_books: pd.DataFrame = self.top_books(
                    df=df
                )
                df_pkl: joblib = convert_and_load_pkl_file(
                    file=top_books,
                    file_path=df_pkl_file_path
                )
                logging.info('top books df to pkl successfully executed....')
                
                logging.info('vector to pkl stated.....')
                vectorize_pkl_file_path : Path = Path(vectorize_file_path)
                vectorize_pkl_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                vectorize_pkl: joblib = convert_and_load_pkl_file(
                    file=vectorize_df,
                    file_path=vectorize_file_path
                )
                logging.info('vector to pkl successfully executed....')    

                data_transformation_artifact: DataTransformationArtifact = DataTransformationArtifact(
                    transformed_df_file_path=df_pkl_file_path,
                    vectorize_file_path=vectorize_pkl_file_path
                )
                
                return data_transformation_artifact
            
        except Exception as e:
            raise MyException(e, sys) from e