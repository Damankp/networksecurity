import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongo(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILEPATH = "Network_Data\phisingData.csv"
    DATABASE = "DAMANAI"
    COLLECTION = "NetworkData"
    Networkobj = NetworkDataExtract()
    records = Networkobj.csv_to_json_converter(file_path=FILEPATH)
    print(records)
    no_of_records = Networkobj.insert_data_to_mongo(records, DATABASE, COLLECTION)
    print(no_of_records)
