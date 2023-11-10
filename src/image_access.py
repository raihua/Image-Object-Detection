import matplotlib.image as mpimg
import os


class ImageAccess:
    def __init__(self, path):
        # Validate the directory path
        self.__validate_directory(path)

        # Extract the directory and filename components
        self.__directory, self.__filename = os.path.split(path)

        # Check if the image file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f'Image file "{path}" does not exist.')

    def read_image(self):
        # Construct the full file path using os.path.join()
        file_path = os.path.join(self.__directory, self.__filename)

        # Read the image data using imread()
        image_data = mpimg.imread(file_path)

        return image_data

    def flatten_and_reshape_image(image_data):
        # Flatten and reshape the image data
        flattened_image = image_data.flatten().reshape(1, -1)
        return flattened_image

    def __validate_directory(self, path):
        # Extract the directory component
        directory = os.path.split(path)[0]

        # Set the allowed directory name
        allowed_directory = "example_images"

        # Check if the directory is the allowed directory
        if directory != allowed_directory:
            raise ValueError(f"Access to directory '{directory}' not permitted.")
