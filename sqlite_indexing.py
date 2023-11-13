import sqlite3
from index_strategy import IndexStrategy
from sqlite_queries import (
    CREATE__IMAGES_TABLE_QUERY,
    CREATE_DETECTED_OBJECTS_TABLE_QUERY,
    INSERT_IMAGE_PATH_PARAM_QUERY,
    SELECT_INCLUDE_ALL_DETECTED,
    SELECT_INCLUDE_SOME_DETECTED,
    INSERT_DETECTED_OBJECTS_PARAM_QUERY,
    SELECT_ALL_IMAGES_OBJECTS_QUERY,
    SELECT_COUNT_PATH,
    SELECT_COUNT_DETECTED,
)


class SQLiteIndexing(IndexStrategy):
    def __init__(self):
        super().__init__()
        self.__conn = sqlite3.connect("memory.db")
        self.__create_table()

    def __create_table(self):
        with self.__conn:
            self.__conn.execute(CREATE__IMAGES_TABLE_QUERY)
            self.__conn.execute(CREATE_DETECTED_OBJECTS_TABLE_QUERY)

    def __execute_and_commit(self, query, params=()):
        with self.__conn:
            self.__conn.execute(query, params)

    def __fetchone(self, query, params):
        cur = self.__conn.execute(query, params)
        return cur.fetchone()[0]

    def add_image_path(self, path):
        if self.__fetchone(SELECT_COUNT_PATH, (path,)) == 0:
            self.__execute_and_commit(INSERT_IMAGE_PATH_PARAM_QUERY, (path,))

    def add_detected_objects(self, image_path, objects):
        if isinstance(objects, str):
            objects = [objects]

        for obj in objects:
            if self.__fetchone(SELECT_COUNT_DETECTED, (image_path, obj)) == 0:
                self.__execute_and_commit(INSERT_DETECTED_OBJECTS_PARAM_QUERY, (image_path, obj))

    def __fetch_all(self, query, params=()):
        cur = self.__conn.execute(query, params)
        return cur.fetchall()

    def __format_results(self, results):
        return {row[0]: row[1].split(",") if row[1] else [] for row in results}

    def get_images_with_all_objects(self, objects) -> dict:
        query = SELECT_INCLUDE_ALL_DETECTED.format(", ".join(["?"] * len(objects)), len(objects))
        return self.__format_results(self.__fetch_all(query, objects))

    def get_images_with_some_objects(self, objects) -> dict:
        query = SELECT_INCLUDE_SOME_DETECTED.format(", ".join(["?"] * len(objects)))
        return self.__format_results(self.__fetch_all(query, objects))

    def get_all_images_and_objects(self) -> dict:
        return self.__format_results(self.__fetch_all(SELECT_ALL_IMAGES_OBJECTS_QUERY))
