from format_strategy import FormatStrategy


class AlphabeticalAscendingFormat(FormatStrategy):
    def __init__(self):
        super().__init__()

    def format_data(self, result_data) -> str:
        sorted_result_data = tuple(
            # Sorts tuples in alphabetical order based on item[0] (path),
            # while also sorting the detected object list alphabetically.
            (item[0], sorted(item[1])) for item in sorted(result_data, key=lambda item: item[0])
        )

        result_str = "\n".join(
            "{}: {}".format(filename, ",".join(objects_list))
            for filename, objects_list in sorted_result_data
        )
        return result_str
