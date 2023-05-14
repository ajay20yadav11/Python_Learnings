"""
given an interget N returns the smallers number with the same number of digits you can assume N is betwen 1 and 10 raise to 9
"""

in1 = input("Enter Number: ")


class OmniCreate:
    def smallest_digit(self, ekahs: int) -> int:
        if not isinstance(ekahs, int):
            ekahs = int(ekahs)

        if len(str(ekahs)) == 1 or int(ekahs) < 0:
            return 0

        return int("9" * (len(str(ekahs)) - 1)) + 1


create = OmniCreate()

print(create.smallest_digit(in1))
