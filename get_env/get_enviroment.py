import os
from dotenv import load_dotenv
from log.logger import logger
from storage.lite.db import StorageInSQLite
from storage.memory.db import StorageInMemory
from error_tracking.env_error import EnvError

class Environment():

    load_dotenv()

    def get_env_storage(self) -> str:
        """Чтение полей 'ENV_STORAGE_TYPE' и 'ENV_STORAGE_FILE_PATH' из environment"""
        return os.environ.get('ENV_STORAGE_TYPE'), os.environ.get('ENV_STORAGE_FILE_PATH')

    def use_storage(self, ENV_STORAGE_TYPE:str, ENV_STORAGE_FILE_PATH:str) -> object:
        """Проверка переменных и инициализация хранилища"""
        try:
            EnvError.check_env_storage_type(ENV_STORAGE_TYPE)
        except EnvError as err:
            logger.warning(err)
            storage = StorageInMemory()
        else:
            match ENV_STORAGE_TYPE:
                case "sqlite":
                    try:
                        EnvError.check_env_storage_file_path(ENV_STORAGE_FILE_PATH)
                    except EnvError as err:
                        logger.critical(err)
                        return err
                    else:
                        storage = StorageInSQLite(ENV_STORAGE_FILE_PATH)
                case "memory":
                    storage = StorageInMemory()
        return storage


