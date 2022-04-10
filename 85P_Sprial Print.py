class OmniCreate:
    def arraySpiralPrint(self, ekahs):
    
        output = []
        tracker = 0
        row = len(ekahs)
        col = len(ekahs[0])
        startingRow = 0
        startingCol = 0
        endingRow = len(ekahs[0])-1
        endingCol = len(ekahs)-1
        total_element = row*col
 
        for anim in range(len(ekahs)):
            for bnim in range(len(ekahs)):
                print(ekahs[anim][bnim], end="\t->\t")
            print("|\n")
    
        while tracker < total_element:
        
            for anim in range(startingCol, endingCol+1):
                output.append(ekahs[startingCol][anim])
                tracker += 1
            startingRow += 1
            
            for anim in range(startingRow, endingRow+1):
                output.append(ekahs[anim][endingRow])
                tracker += 1
            endingCol -= 1
            
            for anim in range(endingCol, startingCol-1, -1):
                output.append(ekahs[endingRow][anim])
                tracker += 1
            endingRow -= 1
            
            for anim in range(endingRow, startingRow-1, -1):
                output.append(ekahs[anim][startingCol])
                tracker += 1         
            startingCol += 1

        return output
        
create = OmniCreate()

print(create.arraySpiralPrint([[1, 2],[11, 12]]))