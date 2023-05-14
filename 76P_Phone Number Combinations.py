class OmniCreate:
    def phoneCombinations(self, ekahs, nokia_dict, index, output, new_output):
        if index == len(ekahs):
            new_output.append(output)
            return

        mapping = nokia_dict[ekahs[index]]

        for anim in range(len(mapping)):
            self.phoneCombinations(
                ekahs, nokia_dict, index + 1, output + mapping[anim], new_output
            )

        return new_output


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
print(create.phoneCombinations("23", nokia_dict, 0, "", new_output))
