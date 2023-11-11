from format_strategy import FormatStrategy


class AlphabeticalAscendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data) -> tuple:
        sorted_result_data = tuple(
            sorted(result_data, key=lambda item: item[0], reverse=False)
        )
        return sorted_result_data
