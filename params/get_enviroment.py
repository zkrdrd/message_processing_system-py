import os
from params.log.logger import logger
from error_tracking.env_error import EnvError
from storage.memory.db import StorageInMemory
from storage.lite.db import StorageInSQLite
from dotenv import load_dotenv

# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
# https://ramziv.com/article/40
# py -m venv .venv
# .venv\Scripts\activate
# deactivate #// deactive venv
# pip install python-dotenv

# https://www.twilio.com/en-us/blog/environment-variables-python
# https://www.google.com/search?q=python+env+variables&sca_esv=8c74246d85a060e1&ei=OT-WZrrCPKzJwPAPsLWrmAI&oq=jghtltktybt+env+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiFmpnaHRsdGt0eWJ0IGVudiBweXRob24qAggAMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogRIzipQiAlY_hRwAngBkAEAmAF0oAGcCaoBAzYuNrgBA8gBAPgBAZgCC6ACjAfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGLEDGA3CAgcQABiABBgNwgIIEAAYogQYiQWYAwCIBgGQBgqSBwM2LjWgB_oz&sclient=gws-wiz-serp
# https://realpython.com/intro-to-pyenv/
# https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
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
                    else:
                        storage = StorageInSQLite(ENV_STORAGE_FILE_PATH)
                case "memory":
                    storage = StorageInMemory()
        return storage


