def Common_Str_Prefix(ekahs: list[str]) -> str:

    output = ''

    for anim in range(len(ekahs[0])):
        for bnim in ekahs:
            if anim == len(bnim) or bnim[anim] != ekahs[0][anim]:
        
                return output
        output += ekahs[0][anim]


    return output


print(Common_Str_Prefix(['flood', 'flower', 'flights']))

