class OutputFormatter:
    def __init__(self, format_strategy):
        self.__strategy = format_strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def validate_k(self, k, image_data):
        if k is not None:
            k = min(k, len(image_data))
            if k < 2:
                raise ValueError("k must be greater than or equal to 2 if provided")
        return k

    def format_and_convert_to_tuple(self, image_data, k=None):
        k = self.validate_k(k, image_data)

        formatted_data = self.__strategy.format_and_convert_to_tuple(image_data)

        if k is not None:
            k_results_data = self.get_top_k_results(formatted_data, k)
            return k_results_data
        else:
            return formatted_data

    def get_top_k_results(self, image_data, k):
        if isinstance(image_data, tuple):
            k_results = image_data[:k]
        else:
            k_results = tuple(list(image_data.items())[:k])

        return k_results
