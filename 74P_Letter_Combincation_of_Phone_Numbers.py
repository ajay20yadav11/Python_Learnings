class OmniCreate:
    def letterCombinations(self, ekahs: str):
        digits_with_letter = {
            "1": " ",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not ekahs:
            return []
        output = [""]
        for anim in ekahs:
            temp = []
            for bnim in digits_with_letter[anim]:
                for cnim in output:
                    temp.append(cnim + bnim)
            print(temp)
            output = temp
        # return output


create = OmniCreate()

print(create.letterCombinations("2345"))
