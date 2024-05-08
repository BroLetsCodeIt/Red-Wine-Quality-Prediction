import os 
import pandas as pd 
from mlProject.entity.config_entity import DataValidationConfig
from src.mlProject.logging import logger

class DataValidation:
    def __init__(self , config : DataValidationConfig):
        self.config = config 


    def validate_all_columns(self)->bool:
        try:
          

            validation_status = None 

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema_keys = self.config.all_schema.keys()
            all_schema_values = self.config.all_schema.values()
            # TODO : also check for types of colums 
            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False
                    with open(self.config.STATUS_FILE , 'w') as f:
                        f.write(f"Validation status : {validation_status}")
                      
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE , 'w') as f:
                        f.write(f'Validation status : {validation_status}')


            return validation_status   
                         
        except Exception as e:
           raise e

