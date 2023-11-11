class OutputFormatter:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def format_data(self, image_data, k=None) -> str:
        formatted_data = self.__strategy.format_data(image_data)

        k = self.__validate_k(k, formatted_data)  # Validate k using the formatted data

        if k is not None:
            k_results_data = self.__get_top_k_results(formatted_data, k)
            formatted_str = "\n".join(
                "{}: {}".format(filename, ",".join(objects))
                for filename, objects in k_results_data.items()
            )
        else:
            formatted_str = "\n".join(
                "{}: {}".format(filename, ",".join(objects))
                for filename, objects in formatted_data.items()
            )

        return formatted_str

    def __validate_k(self, k, image_data) -> int:
        if k is not None:
            k = min(k, len(image_data))
            if k < 2:
                raise ValueError("k must be greater than or equal to 2 if provided")
        return k

    def __get_top_k_results(self, image_data, k) -> dict:
        if k is not None:
            # Sort the formatted_data by values in descending order
            sorted_data = dict(
                sorted(image_data.items(), key=lambda item: item[1], reverse=True)
            )
            k_results = dict(list(sorted_data.items())[:k])
            return k_results
        else:
            return image_data
