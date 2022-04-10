class OmniCreate:
    def greaterRG(self, ekahs):

        output = []

        for anim in range(0, len(ekahs)):
            if anim == len(ekahs)-1:
                output.append(-1)
            else:
                output.append(max(ekahs[anim+1:]))

        return output

create = OmniCreate()

print(create.greaterRG([2, 3, 1, 9]))