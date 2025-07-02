import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self, filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)

            logging.info("converting csv to json formate")

            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def push_data_to_mongodb(self,database, collection, records):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.monogclient = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.monogclient[self.database]
            self.collection = self.database[collection]

            logging.info("inserting data to mongodb atlas" )

            self.collection.insert_many(records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    FilePath = "Network_Data\phisingData.csv"
    DataBase = "YashodeepMore"
    Collection = "NetworkData"
    Network_Object = NetworkDataExtract()
    
    records = Network_Object.csv_to_json_convertor(filepath=FilePath)

    no_of_records = Network_Object.push_data_to_mongodb(records=records, database=DataBase, collection=Collection)

    print(no_of_records)
            