import os
import sys
import joblib
import pandas as pd


from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

from src.exception import MyException
from src.logging import logging
from src.utils.main_utils import convert_and_load_pkl_file
from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def load_vectorize(self, vectorizer_file_path: DataTransformationArtifact) -> pd.pivot_table:
        try:
            vector = convert_and_load_pkl_file(
                file_path=vectorizer_file_path,
                statement='load'
            )
            return vector
        except Exception as e:
            raise MyException(e, sys) from e
    
    def train_model(self, vector: pd.pivot_table) -> cosine_similarity:
        try:
            similarity = cosine_similarity(vector)
            return similarity
        except Exception as e:
            raise MyException(e, sys) from e
        
    def model_trainer_initialize(self, vectorizer_file_path: DataTransformationArtifact, model_file_path: ModelTrainerConfig) -> DataTransformationArtifact:
        try:
            logging.info('Starting Model Training...')
            vector = self.load_vectorize(
                vectorizer_file_path=vectorizer_file_path
            )
            logging.info('Vectirizer file Successfully loaded....')
            
            logging.info('Training the model....')
            model = self.train_model(
                vector=vector
            )
            logging.info('Model Training Successfull....')
            
            model_path: Path = Path(model_file_path)
            model_path.parent.mkdir(parents=True,exist_ok=True)
            model_pkl : joblib = convert_and_load_pkl_file(
                file=model,
                file_path=model_path
            )
            logging.info('model file successfully saved....')
            model_trainer_artifact = ModelTrainerArtifact(
                model_file_path=model_path
            )
            return model_trainer_artifact
            
        except Exception as e:
            raise MyException(e, sys) from e
        
    