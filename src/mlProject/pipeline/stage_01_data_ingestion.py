# create the pipeline 
# matlab konsa function phele run hoga vo decide karne ke liye pipeline likethe hai.


from mlProject.components.data_ingestion import DataIngestion
from mlProject.config.configuration import ConfigurationManager
from mlProject.logging import logger


STAGE_NAME = "Data Ingestion stage"



# class ke ander method ko self likna chiye he.

# normal function ke argument mai self nahi likethe hai.
class DataIngestionTraningPipeline:
     def __init__(self):
          pass
     
     def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()




# why do we use __name__ == '__main__'
# -> because , when we run this file , it will start executing from here. i.e under the __name__ .
# -> if we do not write __name__ == '__main__' 
if __name__ == '__main__':
      try:
        logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<< ')
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n ===========")
      except Exception as e:
           logger.exception(e)
           raise e                    
