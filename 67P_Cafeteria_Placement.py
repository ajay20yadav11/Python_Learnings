class OmniCreate:
    def isTableSafe(self, previous_table, current_table, next_table, K):
        background = []
        if (
            abs(current_table - next_table) > K
            and abs(previous_table - current_table) > K
        ):
            background = [False for cnim in output if abs(cnim - current_table) < K]
        if False in background:
            return False
        else:
            return True

    def cafeteria(self, ekahs, N, K):
        output = ekahs
        place_all_table = [anim for anim in range(N + 1)]
        ekahs.sort()
        start = ekahs[0]
        if len(ekahs) == 1:
            if (ekahs[0] + (K + 1)) <= N:
                ekahs.append(ekahs[0] + (K + 1))
            if (ekahs[0] - (K + 1)) > 0:
                ekahs.insert(0, ekahs[0] - (K + 1))
        for anim in place_all_table:
            background = True
            track_value = 0
            for track_value in range(len(ekahs) - 1):
                if 0 <= anim < start:
                    if abs(anim - start) > K and abs(0 - anim) > K:
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
                elif ekahs[track_value] < anim < ekahs[track_value + 1]:
                    if (
                        abs(anim - ekahs[track_value]) > K
                        and abs(anim - ekahs[track_value + 1]) > K
                    ):
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
                elif ekahs[track_value + 1] < anim <= N:
                    if (
                        abs(anim - ekahs[(len(ekahs) - 1)]) > K
                        and abs(anim - ekahs[track_value + 1]) > K
                    ):
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
        output.sort()
        return output


create = OmniCreate()

create.cafeteria([2, 6], 10, 1)
