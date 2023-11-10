from abc import ABC, abstractmethod


class FormatStrategy(ABC):
    @abstractmethod
    def format_data(self, result_str):
        pass
