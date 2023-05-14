class OmniCreate:
    def phoneCombinations(self, ekahs, nokia_dict):
        comb = [anim for anim in nokia_dict[ekahs[0]]]
        output = []

        for anim in ekahs[1:]:
            temp = []
            for bnim in nokia_dict[anim]:
                temp.append(bnim)

            for cnim in temp:
                for dnim in comb:
                    output.append(cnim + dnim)

        return output


create = OmniCreate()

nokia_dict = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
new_output = []
print(create.phoneCombinations(input("Enter N: "), nokia_dict))
