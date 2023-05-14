from typing import final


class OmniCreate:
    def productDefect(self, ekahs):
        """
        [1 1 1
         1 1 0
         1 0 1]
        """
        output = 0
        final_defect = len(ekahs)
        initial_defect = 0

        if initial_defect < final_defect:
            for anim in range(initial_defect, final_defect):
                for bnim in range(initial_defect, final_defect):
                    print(ekahs[anim][bnim], anim, bnim)
                final_defect -= 1
                initial_defect += 1

        return output


create = OmniCreate()

print(
    create.productDefect(
        [
            [
                1,
                1,
                1,
            ],
            [1, 1, 0],
            [1, 0, 1],
        ]
    )
)
