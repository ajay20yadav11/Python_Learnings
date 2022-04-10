class OmniCreate:

    def letterCombination(self, ekahs: str):

        output = []

        number_word_dict = {2: 'abc',3: 'def', 4: 'ghi', 5:'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        combination_letter = [number_word_dict[int(anim)] for anim in ekahs]

        print(combination_letter, end='\n\n')



        return output

create = OmniCreate()

print(create.letterCombination('23'))
