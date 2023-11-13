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
        self.__cursor = self.__conn.cursor()
        self.create_table()

    def create_table(self):
        self.__cursor.execute(CREATE__IMAGES_TABLE_QUERY)
        self.__cursor.execute(CREATE_DETECTED_OBJECTS_TABLE_QUERY)
        self.__conn.commit()

    def add_image_path(self, path):
        # Check if the image path already exists in the database
        count = self.__cursor.execute(SELECT_COUNT_PATH, (path,)).fetchone()[0]

        if count == 0:
            self.__cursor.execute(INSERT_IMAGE_PATH_PARAM_QUERY, (path,))
            self.__conn.commit()

    def add_detected_objects(self, image_path, objects):
        if isinstance(objects, str):
            objects = [objects]

        for obj in objects:
            # Check if the detected object already exists for the image
            count = self.__cursor.execute(
                SELECT_COUNT_DETECTED, (image_path, obj)
            ).fetchone()[0]

            if count == 0:
                self.__cursor.execute(
                    INSERT_DETECTED_OBJECTS_PARAM_QUERY, (image_path, obj)
                )
                self.__conn.commit()

    def get_images_with_all_objects(self, objects) -> dict:
        # Construct the query by dynamically inserting the objects list into the query template
        query = SELECT_INCLUDE_ALL_DETECTED.format(
            ", ".join(["?"] * len(objects)), len(objects)
        )

        result = self.__cursor.execute(query, objects).fetchall()

        result_dict = {row[0]: row[1].split(",") if row[1] else [] for row in result}

        return result_dict

    def get_images_with_some_objects(self, objects) -> dict:
        # Construct the query by dynamically inserting the objects list into the query template
        query = SELECT_INCLUDE_SOME_DETECTED.format(", ".join(["?"] * len(objects)))

        result = self.__cursor.execute(query, objects).fetchall()

        result_dict = {row[0]: row[1].split(",") if row[1] else [] for row in result}

        return result_dict

    def get_all_images_and_objects(self) -> dict:
        query = SELECT_ALL_IMAGES_OBJECTS_QUERY

        result = self.__cursor.execute(query).fetchall()

        # result is in form {"path": "a, b, c"}
        # this converts it to {"path": ["a", "b", "C"]}
        result_dict = {row[0]: row[1].split(",") if row[1] else [] for row in result}

        return result_dict
