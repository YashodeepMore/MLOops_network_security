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


SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"






"""
Data ingestion related constant start with DATA_INGESTION  Variable name
"""

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "YashodeepMore"
DATA_INGESTION_DIR_NAME:str = "DataIngestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "FeatureStored"
DATA_INGESTION_INGESTED_DIR:str = "Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2




SCHEMA_FILE_PATH = os.path.join('data_schema', 'schema.yaml')

"""
Data validation related constant start with DATA_Validation  Variable name
"""

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessor.pkl"


"""
Data trasnformation related constant  start with DATA_TRANSFORMATION
"""
DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT = "transformed_object"
DATA_TRANSFORMATION_OBJECT_FILE_NAME = "preprocessor.pkl"

#parameters for knn imputer for missing nan values
DATA_TRANSFORMATION_IMPUTER_PARAM:dict = {
    "missing_values" : np.nan,
    "n_neighbors" : 3,
    "weights" : "uniform"
}


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

TRAINING_BUCKET_NAME = "netwworksecurity"