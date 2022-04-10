class OmniCreate:
    def swapNodes(self, head):

        left, right = 0, len(head)-1

        while left < right:
            head[left], head[left+1] = head[left+1], head[left]
            left += 2
            head[right], head[right-1] = head[right-1], head[right]
            right -= 2

        return head


create = OmniCreate()

print(create.swapNodes([1, 2, 3, 4]))