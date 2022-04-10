import csv
import math


class OmniCreate:
    """
    speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
    """

    def Dinasour_Meta(self, filename1, filename2):

        g = 9.8

        dino_lib2, dino_lib1, output = {}, {}, {}

        """
        open1 = open('datasheet2.csv','r').readlines()

        #using by default using readlines()
        for anim in open1:
            NAME, LEG_LENGTH, DIET = anim.split(',')
        """

        # using csv module
        with open(filename2, 'r') as dino1:
            read_file = csv.reader(dino1)

            for anim in read_file:
                NAME, STRIDE_LENGTH, STANCE = anim
                if STANCE == 'bipedal':
                    dino_lib2[NAME] = STRIDE_LENGTH


        with open(filename1, 'r') as dino2:
            read_file2 = csv.reader(dino2)

            for anim in read_file2:
                NAME2, LEG_LENGTH, DIET = anim
                if NAME2 in dino_lib2:
                    dino_lib1[NAME2] = LEG_LENGTH

        print(dino_lib1)
        print(dino_lib2)
        
        #speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
        
        for anim, bnim in dino_lib2.items():
            if anim in dino_lib1:
                
               speed =((float(dino_lib2[anim])/float(dino_lib1[anim])) - 1) * math.sqrt(float(dino_lib1[anim])*float(g))
               print(anim)
               print(speed)
           

create = OmniCreate()

print(create.Dinasour_Meta('datasheet1.csv', 'datasheet2.csv'))
