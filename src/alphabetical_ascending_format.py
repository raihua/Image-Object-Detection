from format_strategy import FormatStrategy


class AlphabeticalAscendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data) -> str:
        # Sort the dictionary items by keys (image paths)
        sorted_result_data = {
            key: sorted(value) for key, value in sorted(result_data.items())
        }

        result_str = "\n".join(
            "{}: {}".format(filename, ",".join(objects_list))
            for filename, objects_list in sorted_result_data.items()
        )
        return result_str
