class OmniCreate:
    def moveAllX(self, ekahs, index, cvalue, output):
        if index == len(ekahs):
            for anim in range(cvalue):
                output.append(0)
            print(output)
            return
        if ekahs[index] == 0:
            cvalue += 1
            self.moveAllX(ekahs, index + 1, cvalue, output)
        else:
            output.append(ekahs[index])
            self.moveAllX(ekahs, index + 1, cvalue, output)


create = OmniCreate()
print(create.moveAllX([1, 0, 1, 1, 0, 0, 1, 1, 1], 0, 0, []))
