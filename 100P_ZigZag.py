class OmniCreate:
    def zigZagTravel(self, ekahs: str, num: int) -> str:
        if num == 1 or num >= len(ekahs):
            return ekahs

        zigzag = ['' for _ in range(num)]
        row = 0
        down = False
        print(zigzag)
        for char in ekahs:
            zigzag[row] += char
            print(zigzag)
            # Change direction when reaching the top or bottom row
            if row == 0 or row == num - 1:
                down = not down

            # Move to the next row based on the direction
            if down:
                row += 1
            else:
                row -= 1

        return ''.join(zigzag)


create = OmniCreate()
print(create.zigZagTravel("PAYPALISHIRING", 3))
