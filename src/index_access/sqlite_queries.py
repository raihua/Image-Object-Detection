CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS Images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_path TEXT,
        detected_objects TEXT
    )
'''

INSERT_IMAGE_PATH = "INSERT INTO Images (image_path) VALUES (?)"

SELECT_DETECTED_OBJECTS = "SELECT detected_objects FROM Images WHERE image_path = ?"

SELECT_IMAGES_ALL_OBJECTS = "SELECT image_path FROM Images WHERE {}"

SELECT_IMAGES_ANY_OBJECTS = "SELECT image_path FROM Images WHERE {}"
