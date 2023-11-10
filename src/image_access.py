import matplotlib.image as mpimg
import os


class ImageAccess:
    def __init__(self, path):
        self.__validate_directory(path)

        self.__path = path

        if not os.path.exists(path):
            raise FileNotFoundError(f'Image file "{path}" does not exist.')

    def read_image(self):
        image_data = mpimg.imread(self.__path)

        return image_data

    # TODO assess whether this is needed
    def flatten_and_reshape_image(self, image_data):
        flattened_image = image_data.flatten().reshape(1, -1)
        return flattened_image

    def __validate_directory(self, path):
        # Extract the directory component
        directory = os.path.split(path)[0]

        allowed_directory = "example_images"

        if directory != allowed_directory:
            raise ValueError(f"Access to directory '{directory}' not permitted.")
