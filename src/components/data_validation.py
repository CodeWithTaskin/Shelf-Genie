import os
import sys
import json
import numpy as np
import pandas as pd

from pathlib import Path
from src.logging import logging
from src.exception import MyException
from src.utils.main_utils import load_yaml_file
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
class DataValidation:
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

    def extract_columns_from_data_and_schema(self, data: pd.DataFrame, schema_file_path: Path) -> list:
        '''
        Method      :       extract_columns_from_data_and_schema.
        Description :       This method extract the data columns and schema columns.
        :params     :       data -> pd.dataframe
        :params     :       schema.yaml file path -> path
        '''
        try:
            df_columns = self.load_data_from_artifact(
                ingested_file_path=data
            ).columns
            schema_columns = load_yaml_file(schema_file_path)['columns']
            logging.info('Columns successfully extracted....')
            return df_columns, schema_columns
        except Exception as e:
            raise MyException(e, sys) from e
        
    def make_report(self, message: str, status: bool, report_file_path: Path) -> json:
        '''
        Method      :       make_report.
        Description :       This method create a validation report and save into desired folder..
        :params     :       message -> str
        :params     :       status -> bool
        :params     :       report_file_path -> Path
        '''
        try:
            report = {
                "message" : message,
                "status" : status
            }
            report_file_path : Path = Path(report_file_path)
            report_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(report_file_path, 'w') as json_file:
                json.dump(report, json_file, indent=4)
            logging.info('Report created Successfully....')
            return report_file_path
        except Exception as e:
            raise MyException(e, sys) from e

    def data_validation_initialize(self, ingested_file_path: Path, schema_file_path: Path, report_file_path: Path):
        '''
        
        '''
        try:
            message: str = ''
            status: bool = ''

            df_columns, schema = self.extract_columns_from_data_and_schema(
                data=ingested_file_path,
                schema_file_path=schema_file_path
            )
            
            if list(df_columns) != schema:
                message = 'Columns are not match'
                status = False
            else:
                status = True
                
            report = self.make_report(
                message=message,
                status=status,
                report_file_path=report_file_path
            )
            
            data_validation_artifact : DataValidationArtifact = DataValidationArtifact(
                validation_report_file_path=report
            )
            return data_validation_artifact
            
        except Exception as e:
            raise MyException(e, sys) from e
        