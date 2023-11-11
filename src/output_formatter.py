class OutputFormatter:
    def __init__(self, format_strategy):
        self.__strategy = format_strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def __validate_k(self, k, image_data) -> int:
        if k is not None:
            k = min(k, len(image_data))
            if k < 2:
                raise ValueError("k must be greater than or equal to 2 if provided")
        return k

    def format_data(self, image_data, k=None) -> tuple:
        k = self.__validate_k(k, image_data)

        formatted_data = self.__strategy.format_data(image_data)

        if k is not None:
            k_results_data = self.__get_top_k_results(formatted_data, k)
            return k_results_data
        else:
            return formatted_data

    def __get_top_k_results(self, image_data, k) -> tuple:
        if isinstance(image_data, tuple):
            k_results = image_data[:k]
        else:
            k_results = tuple(list(image_data.items())[:k])

        return k_results
