from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from pathlib import Path


STAGE_NAME = 'Data Transformaton stage'


class DataTransformationTraningPipeline:
    def __init__(self):
        pass

    def main(self):
                
        try:

            with open(Path('artifacts/data_validation/status.txt') , 'r') as f:
                status = f.read().split(' ')[-1]    # to get the last word
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else :
                raise Exception("Your data schema is not valid")    
        except Exception as e:
            raise e 