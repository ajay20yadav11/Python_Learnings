def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        print(anagram_groups)
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

# Test case
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_words)
print(output)  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
