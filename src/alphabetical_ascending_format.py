from format_strategy import FormatStrategy
from abc import ABC, abstractmethod

class AlphabeticalAscendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data):
        sorted_dict = dict(sorted(result_data.items(), key=lambda item: item[0], reverse=True))
        return sorted_dict