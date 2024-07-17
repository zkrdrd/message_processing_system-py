from parameters.constants import Constants

class EnvError(Exception):
    def check_env_storage_type(ENV_STORAGE_TYPE):
        if ENV_STORAGE_TYPE != Constants.STORAGE_TYPE_SQLITE.value and ENV_STORAGE_TYPE != Constants.STORAGE_TYPE_MEMORY.value:
            raise EnvError('storage type is not found. Using default storage in memory. For switch storage use "ENV_STORAGE_TYPE"')

    def check_env_storage_file_path(ENV_STORAGE_FILE_PATH):
        if ENV_STORAGE_FILE_PATH == "":
            raise EnvError('EnvError: file path for storage is not found. Use "ENV_STORAGE_FILE_PATH" for set it')