import os
import sys
import numpy as np
import pandas as pd

"""
defining common constants variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifact"
FILE_NAME = "PhisingData.csv"
TRAIN_FILE_NAME ="train.csv"
TEST_FILE_NAME = "test.csv"



"""
Data ingestion related constant start with DATA_INGESTION  Variable name
"""

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "YashodeepMore"
DATA_INGESTION_DIR_NAME:str = "DataIngestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "FeatureStored"
DATA_INGESTION_INGESTED_DIR:str = "Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2