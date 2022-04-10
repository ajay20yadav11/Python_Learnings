class OmniCreate:
    def printArrayWave(self, ekahs):

        for anim in range(len(ekahs)):
   
            if (anim%2) == 0:
                tracker = 0
                while tracker < len(ekahs[anim]):
                    print(ekahs[anim][tracker])
                    tracker += 1
            elif (anim%2) == 1:
                tracker = len(ekahs[anim])-1
                while tracker >= 0:
                    print(ekahs[anim][tracker])
                    tracker -= 1

        return ekahs


create = OmniCreate()

print(create.printArrayWave([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))