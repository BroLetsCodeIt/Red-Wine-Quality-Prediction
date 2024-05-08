# pipeline 


from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = 'model_evaluation_stage'


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        try : 
            config = ConfigurationManager() 
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            raise e 