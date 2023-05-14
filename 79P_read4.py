class OmniCreate:
    def toGoatLatin(self, ekahs: str):
        vowel = ["a", "e", "i", "o", "u"]
        last_word = ""

        final_converted = ""

        ekahs_to_list = ekahs.split(" ")
        for anim in ekahs_to_list:
            if anim[0] in vowel:
                final_converted += anim
                final_converted += "ma"
                final_converted += "a"
            else:
                final_converted += anim[1:]
                final_converted += anim[0]
                final_converted += "ma"
                final_converted += "a"

        return final_converted


create = OmniCreate()

print(create.toGoatLatin("I speak Goat Latin"))
