class Solution:
    def lexicalOrder(self, n: int):
        lexOrder = [1]*n
        for i in range(n-1):
            # always consider 0 first
            # ex: 1 -> 10 -> 100
            if  lexOrder[i]*10<=n:
                lexOrder[i+1] = lexOrder[i]*10
            # consider critical point
            # n = 123, previous = 123, current?
            # 122 -> 123 -> 13 (124~129 is not allowed)
            elif lexOrder[i]==n:
                lexOrder[i+1] = lexOrder[i]//10+1
                # eliminate extra 0
                # n = 199, previous = 199, current?
                # ex: 198 -> 199 -> 2
                while lexOrder[i+1]%10==0:
                    lexOrder[i+1] //= 10
            # consider 1 to 9
            # n = 199, previous = 125, current?
            # 124 -> 125 -> 126
            else:
                lexOrder[i+1] = lexOrder[i]+1
                # eliminate extra 0 
                while not lexOrder[i+1]%10:
                    lexOrder[i+1] //= 10
        return lexOrder


Created = Solution()

print(Created.lexicalOrder(20))