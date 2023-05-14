class OmniCreate:
    def subsequence(self, ekahs, index, output, new_set: set()):
        element = 1
        if index == len(ekahs):
            if output in new_set:
                return
            else:
                print(output)
                new_set.add(output)
                return
        self.subsequence(ekahs, index + 1, output + ekahs[index], new_set)
        self.subsequence(ekahs, index + 1, output, new_set)


create = OmniCreate()
new_set = set()
print(create.subsequence("aaabbbccc", 0, "", new_set))
