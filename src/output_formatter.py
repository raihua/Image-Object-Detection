from src.alphabetical_ascending_format import AlphabeticalAscendingFormat
from src.num_descending_format import NumDescendingFormat


class OutputFormatter:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def format_data(self, image_data, k=None) -> str:
        formatted_data = self.__strategy.format_data(image_data)

        if k is not None:
            k_results_data = self.__get_top_k_results(formatted_data, k)
        else:
            k_results_data = formatted_data

        formatted_str = None

        if isinstance(self.__strategy, AlphabeticalAscendingFormat):
            formatted_str = "\n".join(
                "{}: {}".format(filename, ",".join(objects))
                for filename, objects in k_results_data.items()
            )
        elif isinstance(self.__strategy, NumDescendingFormat):
            formatted_str = "\n".join(
                "{} {}".format(value, filename)
                for filename, value in k_results_data.items()
            )
        else:
            formatted_str = "\n".join(
                "{}: {}".format(filename, ",".join(objects))
                for filename, objects in k_results_data.items()
            )

        return formatted_str

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
