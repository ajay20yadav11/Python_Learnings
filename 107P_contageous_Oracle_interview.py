# Find contageous and non contageous
# for e.g. input = 1, 2, 3, 4, 6, 7, 9, 10, 11, 12
# output= 1-4, 6, 7, 9-12

from dataclasses import dataclass
from typing import List


@dataclass
class CheckContageous:
    example_list: List[int]
    build_string = {}

    def filter_for_continuity(self) -> str:
        length_example = len(self.example_list)

        if length_example < 2:
            return [], self.example_list

        in_same_loop = False
        start_value = 0

        for example in range(length_example):
            if not in_same_loop:
                start_value = self.example_list[example]
                self.build_string[start_value] = start_value

            if example == length_example - 1:
                break

            if int(self.example_list[example + 1]) == int(
                self.example_list[example] + 1
            ):
                self.build_string[start_value] = self.example_list[example + 1]
                in_same_loop = True
            else:
                in_same_loop = False

        output_string = ""
        if self.build_string:
            for key, value in self.build_string.items():
                if key == value:
                    output_string += f"{key}, "
                else:
                    output_string += f"{key} - {value}, "

        return output_string[:-2]


if __name__ == "__main__":
    given_data = [1, 2, 3, 4, 6, 8, 9, 10, 11, 12]

    to_filter = CheckContageous(given_data)
    continuoeus = to_filter.filter_for_continuity()
    print(continuoeus)
