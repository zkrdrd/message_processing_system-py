import os
from log.logger import logger
from enum import Enum
from error_tracking.env_error import EnvError
from storage.memory.db import StorageInMemory

# https://www.twilio.com/en-us/blog/environment-variables-python
# https://www.google.com/search?q=python+env+variables&sca_esv=8c74246d85a060e1&ei=OT-WZrrCPKzJwPAPsLWrmAI&oq=jghtltktybt+env+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiFmpnaHRsdGt0eWJ0IGVudiBweXRob24qAggAMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogRIzipQiAlY_hRwAngBkAEAmAF0oAGcCaoBAzYuNrgBA8gBAPgBAZgCC6ACjAfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGLEDGA3CAgcQABiABBgNwgIIEAAYogQYiQWYAwCIBgGQBgqSBwM2LjWgB_oz&sclient=gws-wiz-serp
# https://realpython.com/intro-to-pyenv/
# https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/
class Environment(Enum):

    def get_env_storage():
        return os.environ.get('ENV_STORAGE_TYPE'), os.environ.get('ENV_STORAGE_FILE_PATH')

    def use_storage(ENV_STORAGE_TYPE, ENV_STORAGE_FILE_PATH):
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
                        logger.error(err)
                    else:
                        # TODO
                        # 1. реализовать после добавления sqlite быза
                        pass
                case "memory":
                    storage = StorageInMemory()
        return storage


