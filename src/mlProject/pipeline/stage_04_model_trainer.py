from pathlib import Path 
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from src.mlProject.logging import logger

STAGE_NAME = 'Model Trainer Stage'


class ModelTrainerTrainingPipeline: 
    def __init__(self):
        pass 

    def main(self):

            try: 
                config = ConfigurationManager()
                model_trainer_config = config.get_model_trainer_config()
                model_trainer = ModelTrainer(config=model_trainer_config)
                model_trainer.train()
            except Exception as e : 
                logger.info(e)
                raise e    
            


if __name__ == '__main__':
     try: 
          logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<\n")
          modeltraining = ModelTrainerTrainingPipeline()
          modeltraining.main()
          logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<< \n\n x ============ x")
     except Exception as e: 
          logger.exception(e)
          raise e     
