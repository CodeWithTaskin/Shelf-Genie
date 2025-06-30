import os
import sys

from pathlib import Path
from src.azure.configuration.azure_connection import AzureBlob

from src.logging import logging
from src.exception import MyException

class AzureBlobStorage:
    def __init__(self):
        try:
            self.azure_blob = AzureBlob()
            self.blob_client = self.azure_blob.container()
        except Exception as e:
            raise MyException(e, sys) from e
        
    def upload(self, blob_file_name: str, local_file_path: Path):
        try:
            blob_client = self.blob_client.get_blob_client(blob_file_name)
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data,overwrite=True,timeout=900)
        except Exception as e:
            raise MyException(e, sys) from e
        
    def is_exist(self, blob_file_name: str, container_name: str):
        try:
            blob_client = self.blob_client.get_blob_client(container=container_name, blob=blob_file_name)
            if blob_client.exists():
                logging.info(f"The blob '{blob_file_name}' exists in container '{container_name}'.")
            else:
                logging.info(f"The blob '{blob_file_name}' does NOT exist in container '{container_name}'.")
        except Exception as e:
            raise MyException(e, sys) from e
    
    def download(self, blob_file_name: str, container_name: str, download_file_path: Path):
        try:
            blob_client = self.blob_client.get_blob_client(container=container_name, blob=blob_file_name)

            with open(download_file_path, "wb") as my_blob:
                download_stream = blob_client.download_blob()
                my_blob.write(download_stream.readall())

            logging.info(f"Blob '{blob_file_name}' downloaded successfully to '{download_file_path}'")
        except Exception as e:
            raise MyException(e, sys) from e
        