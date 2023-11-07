class ImageSearchManager():
    def add(self, image_path: str) -> None:
        if not isinstance(image_path, str):
            raise TypeError
        
        


    def search(self, option: str) -> None:
        pass

    def similar(self, k: int, image_path: str) -> None:
        pass

    def list(self) -> list:
        pass

    def set_model(self, model_name: str) -> None:
        pass

    def set_output_format(self, format: str) -> None:
        pass


