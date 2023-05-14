class OmniCreate:
    def toGoatLatin(self, ekahs: str, ekahs_list, anim, final_converted):
        vowel = ["a", "e", "i", "o", "u"]
        counter = 1
        ekahs_list = ekahs.split(" ")

        if anim >= len(ekahs_list):
            return True
        if ekahs_list[anim][0] in vowel:
            final_converted += ekahs_list[anim]
            final_converted += "ma"
        else:
            final_converted += ekahs_list[anim][1:]
            final_converted += ekahs_list[anim][0]
            final_converted += "ma"

        final_converted += "a" * counter
        final_converted += " "
        counter += 1

        self.toGoatLatin(ekahs, ekahs_list, anim + 1, final_converted)

        return final_converted


create = OmniCreate()

print(create.toGoatLatin("The quick brown fox jumped over the lazy dog", "", 0, ""))
