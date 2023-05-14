class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     countS, countT = {}, {}

    #     for anim in range(len(s)):
    #         countS[s[anim]] = 1 + countS.get(s[anim], 0)
    #         countT[t[anim]] = 1 + countT.get(t[anim], 0)
    #     for c in countS:
    #         if countS[c] != countT.get(c,0):
    #             return False

    #     return True
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for anim in range(len(s)):
            counter[ord(s[anim]) - ord("a")] += 1
            counter[ord(t[anim]) - ord("a")] -= 1

        for bnim in counter:
            if bnim != 0:
                return False

        return True


to_validate = Solution()

print(to_validate.isAnagram("anagram", "nagaram"))
