from dataclasses import dataclass
from from_root import from_root
from datetime import datetime
import os
from src.constants import *

@dataclass
class PipelineConfig:
    artefact_folder_path: str = os.path.join(from_root(),ARTEFACT_DIR)
    artifact_dir: str = os.path.join(artefact_folder_path, TIMESTAMP)
    
pipeline_config : PipelineConfig = PipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_folder_path: str = os.path.join(pipeline_config.artifact_dir, DATA_INGESTION_FOLDER_NAME)
    feature_store_folder_path: str = os.path.join(data_ingestion_folder_path, FEATURE_STORE_FOLDER_NAME, FEATURE_STORE_FILE_NAME)
    ingested_folder: str = os.path.join(data_ingestion_folder_path, INGESTED_FOLDER_NAME, INGESTED_FILE_NAME)
    
@dataclass
class DataValidationConfig:
    data_validation_folder_path: str = os.path.join(pipeline_config.artifact_dir, DATA_VALIDATION_REPORT_FOLDER_NAME)
    validation_report_file: str = os.path.join(data_validation_folder_path, VALIDATION_REPORT_FILE)
    schema_file_path: str = os.path.join(from_root(), 'config', 'schema.yaml')
    
@dataclass
class DataTransformationConfig:
    data_transformation_folder_path: str = os.path.join(pipeline_config.artifact_dir, TRANSFORMATION_FOLDER_PATH)
    data_transformed_folder_path: str = os.path.join(data_transformation_folder_path, TRANSFORMED_FOLDER_NAME)
    transformed_df_folder_path: str = os.path.join(data_transformation_folder_path, TRANSFORMED_DF_FOLDER_NAME)
    transformed_df_file_path: str = os.path.join(transformed_df_folder_path, TRANSFORMED_DF_FILE_NAME)
    vectorize_file_path: str = os.path.join(data_transformed_folder_path, TRANSFORMED_FILE_NAME)
    
@dataclass
class ModelTrainerConfig:
    model_trainer_folder_path : str = os.path.join(pipeline_config.artifact_dir, MODEL_TRAINER_FOLDER_PATH)
    model_folder_path : str = os.path.join(model_trainer_folder_path, MODEL_FOLDER_NAME)
    model_file_name : str = os.path.join(model_folder_path, MODEL_FILE_NAME)
    
@dataclass
class ModelPusherConfig:
    model_pusher_folder_path : str = os.path.join(pipeline_config.artifact_dir, MODEL_PUSHER_FOLDER_NAME)
    zip_file_name : str = os.path.join(model_pusher_folder_path, ZIP_FILE_NAME)