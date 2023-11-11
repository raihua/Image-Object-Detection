CREATE__IMAGES_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS Images (
    image_path TEXT PRIMARY KEY
);
"""

CREATE_DETECTED_OBJECTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS Detected_Objects (
    detection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    detected_object TEXT NOT NULL,
    FOREIGN KEY (image_path) REFERENCES Images(image_path),
    UNIQUE (image_path, detected_object)
);
"""

INSERT_IMAGE_PATH_PARAM_QUERY = """
INSERT INTO Images (image_path) VALUES (?);
"""

INSERT_DETECTED_OBJECTS_PARAM_QUERY = """
INSERT INTO Detected_Objects (image_path, detected_object) VALUES (?, ?);
"""

SELECT_INCLUDE_ALL_DETECTED = """
SELECT image_path, GROUP_CONCAT(detected_object) AS detected_objects
FROM Detected_Objects
WHERE detected_object IN ({})
GROUP BY image_path
HAVING COUNT(DISTINCT detected_object) = {};
"""

SELECT_INCLUDE_SOME_DETECTED = """
SELECT image_path, GROUP_CONCAT(detected_object) AS detected_objects
FROM Detected_Objects
WHERE detected_object IN ({})
GROUP BY image_path;
"""

SELECT_ALL_IMAGES_OBJECTS_QUERY = """
SELECT I.image_path, GROUP_CONCAT(DO.detected_object) AS detected_objects
FROM Images AS I
LEFT JOIN Detected_Objects AS DO ON I.image_path = DO.image_path
GROUP BY I.image_path;
"""
