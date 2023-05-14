class OmniCreate:
    def kaitenzushi(self, ekahs: list, K: int):
        output = 0
        prev_output = 0
        dish_stack = []
        track_plate = 0
        condition_to_match = True
        temp_memory_matched_stack = []

        for anim in range(len(ekahs)):
            limiter = 0
            if track_plate == K:
                print("*" * 3)
                condition_to_match = True
                while limiter < K and condition_to_match == True:
                    print("*" * 5, limiter, ekahs[anim - limiter - 1])
                    if ekahs[anim + limiter] in dish_stack:
                        print("*" * 5, ekahs[anim + limiter], dish_stack)
                        output += 1
                        limiter += 1
                    else:
                        dish_stack = []
                        track_plate = 0
                        condition_to_match = False
                if limiter == K:
                    print("*" * 7, "now in final")
                    dish_stack = []
                    track_plate = 0
                    temp_memory_matched_stack = dish_stack
            dish_stack.append(ekahs[anim])
            track_plate += 1
            print(dish_stack, track_plate)

        print(dish_stack)

        return output


create = OmniCreate()

print(create.kaitenzushi([1, 2, 2, 1, 3, 1, 4], 2))
