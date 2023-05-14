class OmniCreate:
    def plusOne(self, digits):
        initial_output = ""

        for anim in digits:
            initial_output += str(anim)

        initial_output = int(initial_output) + 1

        new_digits = []
        new_digits[:0] = str(initial_output)

        digits = [int(anim) for anim in new_digits]

        return digits


create = OmniCreate()

print(create.plusOne([9]))
