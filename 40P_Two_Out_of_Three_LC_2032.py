class OmniCreate:
    def twoOutofThree(self, ekahs: list[int], duva: list[int], tri: list[int]):
        final_term = []

        for anim in range(len(ekahs)):
            if ekahs[anim] in duva or ekahs[anim] in tri:
                if ekahs[anim] not in final_term:
                    final_term.append(ekahs[anim])

        for anim in range(len(duva)):
            if duva[anim] in ekahs or duva[anim] in tri:
                if duva[anim] not in final_term:
                    final_term.append(duva[anim])

        for anim in range(len(tri)):
            if tri[anim] in ekahs or tri[anim] in duva:
                if tri[anim] not in final_term:
                    final_term.append(tri[anim])

        return final_term


create = OmniCreate()

nums1 = [1, 2, 2, 5]
nums2 = [4, 3, 3, 1]
nums3 = [1, 5]

print(create.twoOutofThree(nums1, nums2, nums3))
