import sys
import yaml

from src.exception import MyException

def load_yaml_file(file_path: str)->None:
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise MyException(e, sys) from e