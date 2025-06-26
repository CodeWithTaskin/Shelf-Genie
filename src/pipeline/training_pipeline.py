from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

from src.entity.config_entity import (DataIngestionConfig,
                                      DataValidationConfig)

from src.entity.artifact_entity import (DataIngestionArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config : DataIngestionConfig = DataIngestionConfig()
        self.data_validation_config : DataValidationConfig = DataValidationConfig()
        
    def starting_data_ingestion(self):
        
        data_ingestion: DataIngestion = DataIngestion() 
        data_ingestion_artifact = data_ingestion.data_ingestion_initialize(
            feature_storage_path=self.data_ingestion_config.feature_store_folder_path,
            ingested_path=self.data_ingestion_config.ingested_folder
        )
        
        return data_ingestion_artifact
    
    def starting_data_validation(self, data_ingestion_artifact: DataIngestionArtifact):
        
        data_validation : DataValidation = DataValidation()
        
        data_validation_artifact = data_validation.data_validation_initialize(
            ingested_file_path=data_ingestion_artifact.ingested_file_path,
            schema_file_path=self.data_validation_config.schema_file_path,
            report_file_path=self.data_validation_config.validation_report_file
        )
        return data_validation_artifact
    
    
    def run_pipeline(self):

        start_data_ingestion = self.starting_data_ingestion()
        start_data_validation = self.starting_data_validation(
            data_ingestion_artifact=start_data_ingestion
        )

        
        
        
    