def Common_Str_Prefix(ekahs: list[str]) -> str:
    output = ""

    for anim in range(len(ekahs[0])):
        for bnim in ekahs:
            if anim == len(bnim) or bnim[anim] != ekahs[0][anim]:
                return output
        output += ekahs[0][anim]

    return output

def Common_Str_Prefix(ekahs: list[str]) -> str:
    longest_prefix = ""
    if ekahs:
        return [value for value in zip(*ekahs)]

    for data in range(1, len(ekahs[0])+1):
        curr_pref = [value[:data] for value in ekahs]

        if all(element == curr_pref[0] for element in curr_pref):
            longest_prefix = curr_pref[0]

    return longest_prefix


print(Common_Str_Prefix(["flood", "flower", "flights"]))
