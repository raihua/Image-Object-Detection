from format_strategy import FormatStrategy


class NumDescendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data) -> str:
        sorted_result_data = tuple(
            sorted(result_data, key=lambda item: item[1], reverse=True)
        )
        return sorted_result_data
