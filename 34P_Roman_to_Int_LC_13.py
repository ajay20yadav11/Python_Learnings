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


print(ROM_TO_INT("VIII"))
