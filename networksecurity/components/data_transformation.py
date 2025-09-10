import os
import sys
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAM, TARGET_COLUMN
from networksecurity.entity.artifact_entity import DataValidationArtifat, DataTransformationArtifact
from networksecurity.entity.config_entity import DataTransformationconfig
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object


class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifat, data_transformation_config:DataTransformationconfig):
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def get_data_transformer_object(cls)->Pipeline:
        """
            it initiates knn imputer object with paarameters spe ified in training pipeline.py
            and return pipeline object

            Args*
                cls : DataTransformation
            Returns:
                Pipeline Object
        """
        try:
            logging.info("enterd in get_data_transform_object of Trasnformation class")

            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAM)
            preprocessor = Pipeline([("imputer",imputer)])

            logging.info(f"initiate knn imputer with{DATA_TRANSFORMATION_IMPUTER_PARAM}")
            return preprocessor
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def intiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("entered initiate dat transformation ")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            #training data
            input_features_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=True)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            #test data
            input_features_test_df = train_df.drop(columns=[TARGET_COLUMN], axis=True)
            target_feature_test_df = train_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_train_df.replace(-1,0)

            preprocessor = self.get_data_transformer_object()
            preprocessor_object = preprocessor.fit(input_features_train_df)
            logging.info("created preprocessor_object in intiate data transformation method")

            transformed_input_features_train=preprocessor.transform(input_features_train_df)
            transformed_input_features_test = preprocessor.transform(input_features_test_df)

            train_arr = np.c_[transformed_input_features_train,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_features_test,np.array(target_feature_test_df)]

            #save numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object)
            save_object("final_model/preprocessor.pkl", preprocessor_object)
            logging.info("saved train and test array inside intiate data transformation method")

            #preparing artifacts

            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)