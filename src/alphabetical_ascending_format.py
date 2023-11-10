from format_strategy import FormatStrategy
from abc import ABC, abstractmethod


class AlphabeticalAscendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data):
        sorted_result_data = tuple(
            sorted(result_data.items(), key=lambda item: item[0], reverse=False)
        )
        return sorted_result_data
