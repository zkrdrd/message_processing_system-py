class EnvError(Exception):

    def check_env_storage_file_path(ENV_STORAGE_FILE_PATH) -> Exception:
        """Проверка пути файла хранилища"""
        if ENV_STORAGE_FILE_PATH == "" or ENV_STORAGE_FILE_PATH == None:
            raise EnvError('EnvError: file path for storage is not found. Use "ENV_STORAGE_FILE_PATH" for set it')