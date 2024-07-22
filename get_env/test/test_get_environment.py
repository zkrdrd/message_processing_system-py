from storage.lite.db import StorageInSQLite
from storage.memory.db import StorageInMemory
from get_env.get_enviroment import Environment
from error_tracking.env_error import EnvError

def env(type_torage:str, file_storage:str):
    return Environment().use_storage(type_torage, file_storage)

# 1
def test_env_1():
    assert isinstance(env("memory", ""), StorageInMemory)

# 2
def test_env_2():
    assert isinstance(env("", ""), StorageInMemory)

# 3
def test_env_3():
    assert isinstance(env("sqlite", ""), EnvError)

# 4
def test_env_4():
    assert isinstance(env("sqlite", "./storage/lite/base.db"), StorageInSQLite)