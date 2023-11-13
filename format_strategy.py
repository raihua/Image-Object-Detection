from abc import ABC, abstractmethod


class FormatStrategy(ABC):
    @abstractmethod
    def format_data(self, result_str) -> dict:
        pass

    @abstractmethod
    def format_output(self, data) -> str:
        pass