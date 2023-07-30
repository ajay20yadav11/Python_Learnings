class OmniCreate:
    def findDisappearedNumbers(self, ekahs: list) -> list:
        foundNumber = []
        for anim in range(min(ekahs), max(ekahs) + 1):
            if anim not in ekahs:
                foundNumber.append(anim)

        return foundNumber


create = OmniCreate()

print(create.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 1, 1]))
