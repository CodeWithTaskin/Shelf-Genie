from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    ingested_file_path: Path
    
@dataclass
class DataValidationArtifact:
    validation_report_file_path: Path
    
@dataclass
class DataTransformationArtifact:
    transformed_df_file_path: Path
    vectorize_file_path: Path
    
@dataclass 
class ModelTrainerArtifact:
    model_file_path: Path