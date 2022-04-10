class OmniCreate:
    def reverseString(self, ekahs, cvalue):

        if cvalue == 0:
            print(ekahs[cvalue])
            return 
        
        print(ekahs[cvalue])
        self.reverseString(ekahs, cvalue-1)


create = OmniCreate()

new_string = 'abcd'

print(create.reverseString(new_string, len(new_string)-1))
