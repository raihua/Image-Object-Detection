from index_strategy import IndexStrategy
from sqlite_queries import (
    CREATE__IMAGES_TABLE_QUERY,
    CREATE_DETECTED_OBJECTS_TABLE_QUERY,
    INSERT_IMAGE_PATH_PARAM_QUERY,
    SELECT_INCLUDE_ALL_DETECTED,
    SELECT_INCLUDE_SOME_DETECTED,
    INSERT_DETECTED_OBJECTS_PARAM_QUERY,
    SELECT_ALL_IMAGES_OBJECTS_QUERY,
)


class SQLiteIndexing(IndexStrategy):
    def __init__(self, conn):
        super().__init__()
        self.__conn = conn
        self.__cursor = self.__conn.cursor()
        self.create_table()

    def create_table(self):
        self.__cursor.execute(CREATE__IMAGES_TABLE_QUERY)
        self.__cursor.execute(CREATE_DETECTED_OBJECTS_TABLE_QUERY)
        self.__conn.commit()

    def add_image_path(self, path):
        self.__cursor.execute(INSERT_IMAGE_PATH_PARAM_QUERY, (path,))
        self.__conn.commit()

    def add_detected_objects(self, image_path, objects):
        if isinstance(objects, str):
            objects = [objects]
        values = [(image_path, obj) for obj in objects]
        self.__cursor.executemany(INSERT_DETECTED_OBJECTS_PARAM_QUERY, values)
        self.__conn.commit()

    def get_images_with_all_objects(self, objects) -> list:
        # Construct the query by dynamically inserting the objects list into the query template
        query = SELECT_INCLUDE_ALL_DETECTED.format(
            ", ".join(["?"] * len(objects)), len(objects)
        )

        result = self.__cursor.execute(query, objects).fetchall()

        # ('example_images/image1.jpg',), path at 1st element
        return [row[0] for row in result]

    def get_images_with_some_objects(self, objects) -> list:
        # Construct the query by dynamically inserting the objects list into the query template
        query = SELECT_INCLUDE_SOME_DETECTED.format(", ".join(["?"] * len(objects)))

        result = self.__cursor.execute(query, objects).fetchall()

        # ('example_images/image1.jpg',), path at 1st element
        return [row[0] for row in result]

    def get_all_images_and_objects(self) -> tuple:
        query = SELECT_ALL_IMAGES_OBJECTS_QUERY

        result = self.__cursor.execute(query).fetchall()

        # result is in form {"path": "a, b, c"}
        # this converts it to {"path": ["a", "b", "C"]}
        result_tuple = tuple((row[0], row[1].split(",") if row[1] else []) for row in result)

        return result_tuple