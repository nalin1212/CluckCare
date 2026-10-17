from cluckcare.constants import *
from cluckcare.entity.config_entity import DataIngestionConfig
from cluckcare.utils.common import read_yaml, create_directories
from cluckcare.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(
        self,
    CONFIG_FILEPATH = Path("config/config.yaml"),
        config_filepath = CONFIG_FILEPATH,
        params_filepath = PARAMS_FILEPATH):

        self.config = read_yaml(CONFIG_FILEPATH)
        self.params = read_yaml(PARAMS_FILEPATH)

        create_directories([self.config.artifacts_root])
        self.params = read_yaml(PARAMS_FILEPATH)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
      