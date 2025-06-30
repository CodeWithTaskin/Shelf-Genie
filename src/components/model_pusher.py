import os
import sys
import zipfile

from pathlib import Path
from src.constants import *
from src.logging import logging
from src.exception import MyException
from src.azure.storage.azure_storage import AzureBlobStorage
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, ModelTrainerArtifact, ModelPusherArtifact

class ModelPusher:
    def __init__(self):
        try:
            self.azure_blob_storage = AzureBlobStorage()
        except Exception as e:
            raise MyException(e, sys) from e
        
    def create_path_list(self, *args):
        try:
            path_list = []
            for path in args:
                path_list.append(path)
            return path_list
        except Exception as e:
            raise MyException(e, sys) from e
        
    def model_pusher_initialize(self, ingested_file_path: DataIngestionArtifact, transformed_df_file_path: DataTransformationArtifact, vectorize_file_path: DataTransformationArtifact, model_file_path: ModelTrainerArtifact, zip_file: Path) -> ModelPusherArtifact:
        try:
            logging.info('Starting Model Pusher....')
            required_file_path: ModelPusherArtifact = ModelPusherArtifact(
                ingested_file_path=ingested_file_path,
                transformed_df_file_path=transformed_df_file_path,
                vectorize_file_path=vectorize_file_path,
                model_file_path=model_file_path
            )
            
            logging.info('Listing the Essential file path....')
            path_list = self.create_path_list(
                required_file_path.ingested_file_path,
                required_file_path.transformed_df_file_path,
                required_file_path.vectorize_file_path,
                required_file_path.model_file_path
            )
            
            logging.info('Zipping all the file for upload....')
            zip_file_path : Path = Path(zip_file)
            zip_file_path.parent.mkdir(parents=True,exist_ok=True)
            
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in path_list:
                    if os.path.exists(file_path):
                        zipf.write(file_path, os.path.basename(file_path))
            logging.info('Zipping Successful....')
            
            logging.info('Uploading on Azure Blob Storage....')
            azure_upload = self.azure_blob_storage.upload(
                blob_file_name=ZIP_FILE_NAME,
                local_file_path=zip_file_path
            )
            logging.info('Successfully Uploaded....')
            logging.info('Model Pusher Successfully Executed....')
            return azure_upload
        except Exception as e:
            raise MyException(e, sys) from e