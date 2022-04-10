class OmniCreate:
    def reverseString(self, s: list[StopIteration]):

        left, right = 0, len(s)-1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

    

create = OmniCreate()

print(create.reverseString(['a', 'e', 'i', 'o', 'u', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 6, 4, 2, 4, 7]))