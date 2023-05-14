class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha_dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

        num_firstWord, num_secondWord, num_targetWord = "", "", ""

        for anim in firstWord:
            num_firstWord += str(alpha_dict.index(anim))

        for anim in secondWord:
            num_secondWord += str(alpha_dict.index(anim))

        for bnim in targetWord:
            num_targetWord += str(alpha_dict.index(bnim))

        print(num_firstWord)
        print(num_secondWord)
        print(num_targetWord)

        if int(num_targetWord) == (int(num_firstWord) + int(num_secondWord)):
            return True

        return False


create = Solution()

print(create.isSumEqual("j", "j", "bi"))
