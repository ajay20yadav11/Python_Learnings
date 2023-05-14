def longestPalindrome(ekahs):
    output = ""
    outputleg = 0

    for anim in range(len(ekahs)):
        left, right = anim, anim
        while left > anim and right < len(ekahs) and ekahs[left] == ekahs[right]:
            if (right - left + 1) > outputleg:
                output = ekahs[left : right + 1]
                outputleg = right - left + 1
            left -= 1
            right += 1

        left, right = anim, anim + 1
        while left > anim and right < len(ekahs) and ekahs[left] == ekahs[right]:
            if (right - left + 1) > outputleg:
                output = ekahs[left : right + 1]
                outputleg = right - left + 1
            left -= 1
            right += 1

    return output


print(longestPalindrome("dabab"))
