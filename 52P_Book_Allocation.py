class OmniCreate:
    def Book_Allocation(self, A, B):
        dump_addition = []

        iter = 1

        while iter < len(A):
            dump_addition.append((sum(A[:iter]), sum(A[iter:])))
            iter += 1

        output = []
        print(dump_addition)
        for anim in dump_addition:
            output.append(max(anim))

        return min(output)


create = OmniCreate()

print(
    create.Book_Allocation([12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 134, 67, 90, 22, 11, 33], 4)
)
