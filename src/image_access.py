from matplotlib.image import imread
import os


class ImageAccess:
    def __init__(self, directory):
        self.__allowed_directory = "example_images"  # Set the allowed directory name
        if directory != self.__allowed_directory:
            raise ValueError("Access to directory not permitted")
        self.__directory = directory

    def read_image(self, file_name):
        # Construct the full file path
        file_path = os.path.join(self.__directory, file_name)
        image_data = imread(file_path)
        return image_data
