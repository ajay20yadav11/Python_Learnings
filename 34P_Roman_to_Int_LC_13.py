def ROM_TO_INT(ekahs: str) -> int:
    data_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    final_converted = 0

    for anim in range(len(ekahs)):
        if (
            anim + 1 < len(ekahs)
            and data_dict[ekahs[anim]] < data_dict[ekahs[anim + 1]]
        ):
            final_converted -= data_dict[ekahs[anim]]
        else:
            final_converted += data_dict[ekahs[anim]]

    return final_converted


def rommon_to_int(rommon):

    data_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for r in range(len(rommon)):
        if (r+1 < len(rommon)) and data_dict[rommon[r]] < data_dict[rommon[r+1]]:
            number -= data_dict[rommon[r]]
        else:
            number += data_dict[rommon[r]]

    return number


print(ROM_TO_INT("VIII"))
print(rommon_to_int("IX"))
