class OmniCreate:
    def Valid_Parentheses(self, ekahs: str) -> bool:
        if len(ekahs) == 0 or len(ekahs) == 1:
            return False

        ekahs = ekahs.replace(")", "(")
        ekahs = ekahs.replace("]", "[")
        ekahs = ekahs.replace("}", "{")

        while len(ekahs) != 0:
            initial = ekahs[0]
            final = ekahs[-1]
            if ord(initial) != ord(final):
                return False
            ekahs = ekahs[1:]
            ekahs = ekahs[:-1]

        return True


Create = OmniCreate()

print(Create.Valid_Parentheses("([{}])"))
