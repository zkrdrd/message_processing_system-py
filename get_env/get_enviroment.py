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

    def use_storage(self, env_storage_type:str, env_storage_file_path:str) -> object:
        """Проверка переменных и инициализация хранилища"""
        match env_storage_type:
            case "sqlite":
                try:
                    EnvError.check_env_storage_file_path(env_storage_file_path)
                except EnvError as err:
                    logger.critical(err)
                    return err
                else:
                    storage = StorageInSQLite(env_storage_file_path)
            case "memory":
                storage = StorageInMemory()
            case _:
                logger.warning('storage type is not found. Using default storage in memory. For switch storage use "ENV_STORAGE_TYPE"')
                storage = StorageInMemory()
        return storage


