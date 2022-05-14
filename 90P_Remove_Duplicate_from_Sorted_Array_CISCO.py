# # Remove all Duplicate Number with individual
# class Omnicreate:

#     def remove_all_duplicate(self, ekahs):

#         while ekahs:
#             new_ekash = list()

#             min_val = min(ekahs)

#             for anim in ekahs:

#                 if anim != min_val:

#                     new_ekash.append(anim)

#             ekahs = [anim-min_val for anim in new_ekash]

#             print('Minimum of array is ' + str(min_val) + ' and now the final arrary: ' + str(ekahs))



# create = Omnicreate()

animated = [1, 2, 2, 3, 4, 5, 5, 5, 6, 3, 2]

# print(create.remove_all_duplicate(animated))



for anim, bnim in enumerate(animated):

    