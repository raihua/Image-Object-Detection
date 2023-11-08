CREATE__IMAGES_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS Images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT NOT NULL
);
"""

CREATE_DETECTED_OBJECTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS Detected_Objects (
    detection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    detected_object TEXT NOT NULL,
    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);
"""

INSERT_IMAGE_PATH_PARAM_QUERY = """
INSERT INTO Images (image_path) VALUES (?);
"""

SELECT_INCLUDE_ALL_DETECTED = """
SELECT Images.image_path, Detected_Objects.detect_object
FROM Images
LEFT JOIN Detected_Objects ON Images.image_path = Detected_Objects.image_path;
"""