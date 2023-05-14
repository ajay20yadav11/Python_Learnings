class OmniCreate:
    def plusOne(self, ekahs):
        if len(ekahs) == 0:
            return -1

        initial_output = ""

        for anim in ekahs:
            initial_output += str(anim)

        initial_output = int(initial_output) + 1

        ekahs = []
        ekahs = [int(anim) for anim in str(initial_output)]

        return ekahs


create = OmniCreate()

print(create.plusOne([1, 2, 3]))
