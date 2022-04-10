class OmniCreate:
    def rotatearray_90_Degree(self, ekahs: list):
        
        output = [[0 for _ in range(len(ekahs))] for _ in range(len(ekahs))]
        
        for anim in range(len(ekahs)):
            for bnim in range(len(ekahs[anim])):
                print(ekahs[anim][bnim], end="\t")
            print('\n')
        
        for anim in range(len(ekahs)):
            for bnim in range(len(ekahs[anim])):
                output[anim][bnim] = ekahs[len(ekahs)-1-bnim][anim]

        print('*'*15)

        for anim in range(len(output)):
            for bnim in range(len(output[anim])):
                print(output[anim][bnim], end="\t")
            print('\n')
        
        
        return 
    
create = OmniCreate()

print(create.rotatearray_90_Degree([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
