import os
import sys

from azure.storage.blob import BlobServiceClient

from src.constants import *
from src.logging import logging
from src.exception import MyException

class AzureBlob:
    def __init__(self):
        try:
            logging.info('Connecting to Azure Blob....')
            blob_service_client = BlobServiceClient.from_connection_string(conn_str=os.getenv('AZURE_STORAGE_CONNECTION_STRING'))
            self.container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)
            logging.info('Successfully Connected to Azure Blob.....')
        except Exception as e:
            raise MyException(e, sys) from e
        
    def container(self):
        try:
            return self.container_client
        except Exception as e:
            raise MyException(e, sys) from e
    