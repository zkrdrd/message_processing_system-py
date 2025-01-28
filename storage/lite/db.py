import sqlite3
from types import SimpleNamespace
from log.logger import logger
from models.payment import Payment


class StorageInSQLite:

    def __init__(self, storage_file_path: str) -> None:
        """Инициализация хранилища"""

        self.__create_base = [
            """CREATE TABLE IF NOT EXISTS payment
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_message TEXT NOT NULL,
        uid_message TEXT NOT NULL UNIQUE,
        address_from TEXT NULL,
        address_to TEXT NULL,
        amount INTEGER NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NULL);"""
        ]

        self.__sqlite_storage = storage_file_path

        try:
            with sqlite3.connect(self.__sqlite_storage) as self.__connect:
                self.__cursor = self.__connect.cursor()
                for var in self.__create_base:
                    self.__cursor.execute(var)
                self.__connect.commit()
        except sqlite3.Error as err:
            logger.critical(err)
            return err

    def save_payment(self, payment: Payment) -> None:
        """Сохранение данных в хранилище"""

        self.__query_insert_update = """
    INSERT INTO payment (type_message, uid_message, address_from,
    address_to, amount, created_at, updated_at)
    VALUES (
        ?, -- type_message
        ?, -- uid_message
        ?, -- address_from
        ?, -- address_to
        ?, -- amount
        ?, -- created_at
        ?) -- updated_at
    ON CONFLICT DO UPDATE SET
        type_message = EXCLUDED.type_message,
        updated_at = EXCLUDED.updated_at;"""

        self.__save_payment_fields = (
            payment.type_message,
            payment.uid_message,
            payment.address_from,
            payment.address_to,
            payment.amount,
            payment.created_at,
            payment.updated_at,
        )

        try:
            with sqlite3.connect(self.__sqlite_storage) as self.__connect:
                self.__connect.cursor().execute(
                    self.__query_insert_update, self.__save_payment_fields
                )
                self.__connect.commit()
        except sqlite3.Error as err:
            logger.critical(err)
            return err

    def get_payment_by_id(self, id: str) -> Payment:
        """Получение данных из хранилища по id"""

        self.__query_select = """SELECT type_message, uid_message,
    address_from, address_to, amount, created_at, updated_at
    FROM payment WHERE uid_message = ?;"""

        try:
            with sqlite3.connect(self.__sqlite_storage) as self.__connect:
                __cursor = self.__connect.cursor()
                __cursor.execute(self.__query_select, (id,))
                self.__columns = [column[0] for column in __cursor.description]
                self.__values = __cursor.fetchone()
                if self.__columns is None or self.__values is None:
                    return None
                else:
                    self.__row_dict = dict(zip(self.__columns, self.__values))
                    self.__row_dict = SimpleNamespace(**self.__row_dict)
                    return self.__row_dict
                # connect.row_factory = sqlite3.Row
                # self.__getted_payment = \
                # connect.cursor().execute(self.__query_select, (id,))\
                # .fetchone()
                # self.__getted_payment_dict:dict = \
                # dict(eval(self.__getted_payment))
        except sqlite3.Error as err:
            logger.critical(err)
            return err
