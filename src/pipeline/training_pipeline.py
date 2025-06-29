
from src.logging import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation

from src.entity.config_entity import (DataIngestionConfig,
                                      DataValidationConfig,
                                      DataTransformationConfig)

from src.entity.artifact_entity import (DataIngestionArtifact,
                                        DataValidationArtifact,
                                        DataTransformationArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config : DataIngestionConfig = DataIngestionConfig()
        self.data_validation_config : DataValidationConfig = DataValidationConfig()
        self.data_transformation_config: DataTransformationConfig = DataTransformationConfig()
        
    def starting_data_ingestion(self):
        
        data_ingestion: DataIngestion = DataIngestion() 
        data_ingestion_artifact = data_ingestion.data_ingestion_initialize(
            feature_storage_path=self.data_ingestion_config.feature_store_folder_path,
            ingested_path=self.data_ingestion_config.ingested_folder
        )
        
        return data_ingestion_artifact
    
    def starting_data_validation(self, data_ingestion_artifact: DataIngestionArtifact):
        
        data_validation : DataValidation = DataValidation()
        logging.info('Data Validation Started...')
        data_validation_artifact = data_validation.data_validation_initialize(
            ingested_file_path=data_ingestion_artifact.ingested_file_path,
            schema_file_path=self.data_validation_config.schema_file_path,
            report_file_path=self.data_validation_config.validation_report_file
        )
        logging.info('Data Validation Executed Successfully....')
        return data_validation_artifact
    
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact, data_ingestion_artifact: DataIngestionArtifact):
        
        data_transformation : DataTransformation = DataTransformation()
        
        data_transformation_artifact = data_transformation.data_transformation_initialize(
            report_file=data_validation_artifact.validation_report_file_path,
            ingested_file_path=data_ingestion_artifact.ingested_file_path,
            transformed_df_file_path=self.data_transformation_config.transformed_df_file_path,
            vectorize_file_path=self.data_transformation_config.vectorize_file_path
        )
        
        return data_transformation_artifact
    
    
    def run_pipeline(self):

        start_data_ingestion = self.starting_data_ingestion()
        start_data_validation = self.starting_data_validation(
            data_ingestion_artifact=start_data_ingestion
        )
        start_data_transformation = self.start_data_transformation(
            data_ingestion_artifact=start_data_ingestion,
            data_validation_artifact=start_data_validation
        )

        
        
        
    