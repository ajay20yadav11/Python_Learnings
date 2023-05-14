"""
Write a function solution that gives S consisiting of N letters 'a' and/or 'b' returns True when all occcurences of letter a are before all occurences of letter b and tetruens false otherwise
S='aabbb' returns 1 
S = 'ba' returns 0
S = 'aaa' returns 1
S= 'b' returns 1
"""


edge_cases = [
    "aabbba",  # Returns False
    "aabbbb",  # Returns True
    "aaaabbb",  # Returns True
    "ab",  # Returns True
    "ba",  # Returns False
    "aaaa",  # Returns True
    "bbbb",  # Returns True
    "ababab",  # Returns True
    "baba",  # Returns False
    "a",  # Returns True
    "",  # Returns True
    "a@b#c",  # Returns True
    "a@b@%b%^a^%^&@$c",  # Returns False
]


class OmniCreate:
    def occr_before_another(self, ekahs):
        dummpy_ekahs = [
            ekahs[anim] for anim in range(len(ekahs)) if ekahs[anim].isalpha()
        ]

        for anim in range(len(dummpy_ekahs) - 1):
            if ord(dummpy_ekahs[anim]) > ord(dummpy_ekahs[anim + 1]):
                return False

        return True


create = OmniCreate()

output = [create.occr_before_another(edge) for edge in edge_cases]

print(output)
