def deci_to_bina(ekahs):
    assert int(ekahs) == ekahs, "The number must be integer"

    if ekahs == 0:
        return 0
    else:
        return ekahs % 2 + 10 * deci_to_bina(int(ekahs / 2))


print(deci_to_bina(int(input("Enter number to convert in binary: "))))
