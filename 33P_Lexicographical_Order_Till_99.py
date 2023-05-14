class Lexi_Sort:
    def Bubble_Sort(ekahs):
        for anim in range(len(ekahs)):
            for bnim in range(len(ekahs) - 1 - anim):
                if ekahs[bnim] > ekahs[bnim + 1]:
                    ekahs[bnim], ekahs[bnim + 1] = ekahs[bnim + 1], ekahs[bnim]

        return ekahs

    def Lexicographical_Sort(self, value_of_n):
        dict_duva = {}

        for anim in range(1, value_of_n + 1):
            if anim // 10 == 0:
                dict_duva[anim] = []
            if anim // 10 != 0:
                dict_duva[anim // 10].append(anim)

        for key, val in dict_duva.items():
            dict_duva[key] = Lexi_Sort.Bubble_Sort(val)

        # print(dict_duva)

        duva = []

        for key, val in dict_duva.items():
            duva.append(key)
            for anim in val:
                duva.append(anim)

        return duva


Created = Lexi_Sort()
print(Created.Lexicographical_Sort(99))
