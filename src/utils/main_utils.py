import sys
import yaml
import joblib
import json
from pathlib import Path


from src.exception import MyException



def load_yaml_file(file_path: str)->None:
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
        
    except Exception as e:
        raise MyException(e, sys) from e

def convert_to_pkl_file(file: object, file_path: Path)-> joblib:
    try:
        joblib.dump(file, open(file_path, 'wb'))
        
    except Exception as e:
        raise MyException(e, sys) from e
    
def load_json(file_path: object) -> json:
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)
        return config_data
    except Exception as e:
        raise MyException(e, sys) from e
    