from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTraningPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.logging import logger

from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline 
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTraningPipeline   
STAGE_NAME = "Data Ingestion stage"



try:
        logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<< ')
        data_ingestion = DataIngestionTraningPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n ===========")
except Exception as e:
           logger.exception(e)
           raise e  




STAGE_NAME ='Data Validation Stage'


try: 
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        data_validation = DataValidationTraningPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n x ============= x")
except Exception as e : 
        logger.exception(e)
        raise e  



STAGE_NAME = 'Data Transformation Stage'

try: 
     logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
     data_transformation = DataTransformationTraningPipeline()
     data_transformation.main()
     logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ==============x ")

except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = 'Model Trainer Stage'

try: 
          logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<\n")
          modeltraining = ModelTrainerTrainingPipeline()
          modeltraining.main()
          logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<< \n\n x ============ x")
except Exception as e: 
          logger.exception(e)
          raise e    





STAGE_NAME = 'Model Evaluation Stage'

try : 
            config = ConfigurationManager() 
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
except Exception as e:
            raise e 