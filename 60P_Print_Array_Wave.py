class OmniCreate:
    def printArrayWave(self, ekahs):
        for anim in range(len(ekahs)):
            if (anim % 2) == 0:
                tracker = 0
                while tracker < len(ekahs[anim]):
                    print(ekahs[anim][tracker])
                    tracker += 1
            elif (anim % 2) == 1:
                tracker = len(ekahs[anim]) - 1
                while tracker >= 0:
                    print(ekahs[anim][tracker])
                    tracker -= 1

        return ekahs


create = OmniCreate()

print(create.printArrayWave([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))




class OmniCreate:
    def printArrayWave(self, ekahs):
        for anim in range(len(ekahs)):
            travel = 0 if anim % 2 == 0 else len(ekahs[anim])-1
            condTravel = True if not travel else False
            while True:
                if condTravel:
                    print(ekahs[anim][travel])
                    travel += 1
                else:
                    print(ekahs[anim][travel])
                    travel -= 1

                if travel == len(ekahs[anim]) or travel < 0:
                    break

        return ekahs


create = OmniCreate()

print(create.printArrayWave([[1, 2, 3], 
                             [4, 5, 6], 
                             [7, 8, 9]]))



