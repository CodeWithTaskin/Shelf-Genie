import os
import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

from src.constants import *
from src.logging import logging
from src.exception import MyException

class MongoDBConnection:
    def __init__(self, db_name: str, collection_name: str, connection_url: str):
        try:
            logging.info('Connecting with MongoDB....')
            self.client = MongoClient(connection_url)
            
            status = self.client.admin.command('ping')
            if status['ok'] == 1:
                self.db = self.client[db_name]
                self.collection = self.db[collection_name]
                logging.info('MongoDB connected Successfully....')
            
        except ConnectionFailure as e:
            raise MyException(e, sys) from e
        
        except OperationFailure as e:
            raise MyException(e, sys) from e  
             
        except Exception as e:
            raise MyException(e, sys) from e