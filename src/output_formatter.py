class OutputFormatter:
    def __init__(self, format_strategy):
        self.__strategy = format_strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def format_data(self, image_data):
        return self.__format_strategy.format_data(image_data)