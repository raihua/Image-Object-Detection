import matplotlib.image as mpimg
import numpy as np
import os


class ImageAccess:
    def read_image(self, path) -> np.ndarray:
        self.__validate_directory(path)
        image_data = mpimg.imread(path)
        return image_data

    # TODO assess whether this is needed
    def flatten_and_reshape_image(self, image_data) -> np.ndarray:
        flattened_image = image_data.flatten().reshape(1, -1)
        return flattened_image

    def __validate_directory(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f'Image file "{path}" does not exist.')
        # Extract the directory component
        directory = os.path.split(path)[0]

        allowed_directory = "example_images"

        if directory != allowed_directory:
            raise ValueError(f"Access to directory '{directory}' not permitted.")
