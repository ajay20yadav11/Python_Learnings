# class Solution:
#     # def isAnagram(self, s: str, t: str) -> bool:
#     #     if len(s) != len(t):
#     #         return False

#     #     countS, countT = {}, {}

#     #     for anim in range(len(s)):
#     #         countS[s[anim]] = 1 + countS.get(s[anim], 0)
#     #         countT[t[anim]] = 1 + countT.get(t[anim], 0)
#     #     for c in countS:
#     #         if countS[c] != countT.get(c,0):
#     #             return False

#     #     return True
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         counter = [0] * 26

#         for anim in range(len(s)):
#             counter[ord(s[anim]) - ord("a")] += 1
#             counter[ord(t[anim]) - ord("a")] -= 1

#         for bnim in counter:
#             if bnim != 0:
#                 return False

#         return True


# to_validate = Solution()

# print(to_validate.isAnagram("anagram", "nagaram"))


def is_anagram(s1, s2):
    # Remove spaces and convert both strings to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # If the lengths of the strings are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Create a dictionary to count character occurrences in s1
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    # Check if each character in s2 exists in char_count and decrement its count
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1


    return True






def is_anagram(s1: str, s2: str) -> bool:

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    char_dict = {}
    for char in s1:
        char_dict.setdefault(char, 0)
        char_dict[char] += 1

    for char in s2:
        if (char not in char_dict) or char_dict[char] ==  0:
            return False
        char_dict[char] += 1

    return True



# Test cases
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
print(is_anagram("Astronomer", "Moon starer"))  # Output: True
    