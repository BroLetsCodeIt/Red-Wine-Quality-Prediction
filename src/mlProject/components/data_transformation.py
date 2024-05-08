# create the component

import os 
from mlProject.entity.config_entity import DataTransformationConfig
from src.mlProject.logging import logger 

from sklearn.model_selection import train_test_split  # type: ignore
import pandas as pd  # type: ignore

class DataTransformation:
    def __init__(self , config : DataTransformationConfig):
        self.config = config 


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
       
        # we can add different data transformation technique such as scalar , PCA  and  all
        # we call perform all kinds of EDA in ML cycle  here before passing  this data to the model

        # splitting the data in train and test sets.(0.75 , 0.25) split.

        train , test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir , 'train.csv') , index = False)
        test.to_csv(os.path.join(self.config.root_dir , 'test.csv') , index = False)

        logger.info("splitted data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)