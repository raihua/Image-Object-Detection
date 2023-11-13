from alphabetical_ascending_format import AlphabeticalAscendingFormat
from num_descending_format import NumDescendingFormat


class OutputFormatter:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def format_data(self, image_data, k=None) -> str:
        formatted_data = self.__strategy.format_data(image_data)
        k_results_data = self.__get_top_k_results(formatted_data, k) if k is not None else formatted_data
        return self.__format_strategy_specific(k_results_data)

    def __get_top_k_results(self, image_data, k) -> dict:
        return dict(sorted(image_data.items(), key=lambda item: item[1], reverse=True)[:k])

    def __format_strategy_specific(self, data) -> str:
        return self.__strategy.format_output(data)
