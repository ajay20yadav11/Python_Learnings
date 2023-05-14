from typing import final


class OmniCreate:
    def cafeteria(self, S, N, K):
        final_output = []
        output = S
        place_all_table = [anim for anim in range(N + 1)]
        S.sort()
        start = S[0]
        if len(S) == 1:
            if (S[0] + (K + 1)) <= N:
                S.append(S[0] + (K + 1))
            if (S[0] - (K + 1)) > 0:
                S.insert(0, S[0] - (K + 1))
        for anim in place_all_table:
            background = True
            track_value = 0
            for track_value in range(len(S) - 1):
                if 0 <= anim < start:
                    if abs(anim - start) > K and abs(0 - anim) > K:
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
                            final_output.append(anim)
                elif S[track_value] < anim < S[track_value + 1]:
                    if (
                        abs(anim - S[track_value]) > K
                        and abs(anim - S[track_value + 1]) > K
                    ):
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
                            final_output.append(anim)
                elif S[track_value + 1] < anim <= N:
                    if (
                        abs(anim - S[(len(S) - 1)]) > K
                        and abs(anim - S[track_value + 1]) > K
                    ):
                        background = [
                            False for cnim in output if abs(cnim - anim) < K + 1
                        ]
                        if False not in background:
                            output.append(anim)
                            final_output.append(anim)
        output.sort()
        return len(final_output)


create = OmniCreate()

print(create.cafeteria([6, 10, 14], 15, 2))
