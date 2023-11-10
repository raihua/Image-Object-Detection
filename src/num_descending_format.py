from format_strategy import FormatStrategy
from abc import ABC, abstractmethod


class NumDescendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data):
        sorted_result_data = dict(
            sorted(result_data.items(), key=lambda item: item[1], reverse=True)
        )
        return sorted_result_data
