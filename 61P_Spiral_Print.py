class OmniCreate:
    def arraySpiral_Print(self, ekahs):

        print(ekahs)
        print("\n"*3)
        output = None
        top, bottom, left, right = 0, len(ekahs) -1 , 0, len(ekahs) - 1


        while top <= bottom and left <= right:

            # Travel on 0th index of overall array till last
            for anim in range(left, right + 1):
                print(ekahs[top][anim])
            
            top += 1

             # go down printing last within index till last overall array

            for anim in range(top, bottom + 1):
                print(ekahs[anim][right])

            right -= 1

            # print(left, right, top, bottom)

            # if top <= bottom:
            for anim in range(right, left - 1, -1):
                print(ekahs[bottom][anim])
            bottom -= 1

            # Print the leftmost column (in reverse)
            # if left <= right:
            for anim in range(bottom, top - 1, -1):
                print(ekahs[anim][left])
            left += 1



        return None


create = OmniCreate()

create.arraySpiral_Print([[1, 2, 3],
                          [4, 5, 6], 
                          [7, 8, 9]])
