def encode(ekahs):
    output = ""
    for anim in range(len(ekahs)):
        output += str(len(ekahs[anim])) + "#" + ekahs[anim]

    return output


def decode(ekahs):
    output, anim = [], 0

    while anim < len(ekahs):
        bnim = anim
        while ekahs[bnim] != "#":
            bnim += 1
        leg = int(ekahs[anim:bnim])
        output.append(ekahs[(bnim + 1) : (bnim + 1 + leg)])
        anim = bnim + 1 + leg

    return output


platform = ["lint", "code", "love", "you"]
encoded_platform = encode(platform)
print(encoded_platform)
decoded_platform = decode(encoded_platform)
print(decoded_platform)
