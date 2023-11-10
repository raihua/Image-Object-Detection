from abc import ABC, abstractmethod


class FormatStrategy(ABC):
    @abstractmethod
    def format_and_convert_to_tuple(self, result_str):
        pass
