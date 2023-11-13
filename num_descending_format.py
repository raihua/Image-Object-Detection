from format_strategy import FormatStrategy


class NumDescendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data) -> dict:
        # Sort the dictionary items by values in descending order
        sorted_result_data = dict(
            sorted(result_data.items(), key=lambda item: item[1], reverse=True)
        )

        return sorted_result_data

    def format_output(self, data) -> str:
            return "\n".join("{:.4f} {}".format(value, filename) for filename, value in data.items())