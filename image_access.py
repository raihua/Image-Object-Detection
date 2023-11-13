import matplotlib.image as mpimg
import numpy as np
import os


class ImageAccess:
    def __init__(self, allowed_directory="example_images"):
        self.__allowed_directory = allowed_directory

    def read_image(self, path) -> np.ndarray:
        self.__validate_file_existence(path)
        self.__validate_directory_access(path)
        return mpimg.imread(path)

    def __validate_file_existence(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f'Image file "{path}" does not exist.')

    def __validate_directory_access(self, path):
        directory = os.path.dirname(path)
        if directory != self.__allowed_directory:
            raise ValueError(f"Access to directory '{directory}' not permitted.")
