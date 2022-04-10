#To calculate Longest Common SubSequence
#input1: animated
#input2: bnimapoi

from inspect import trace


class OmniCreate:
    def longestSubSequence_iteration(self, ekahs, duva):
        
        
        dp = [[0 for anim in range(len(ekahs)+1)] for bnim in range(len(duva)+1)]

        for anim in range(len(duva)):
            for bnim in range(len(ekahs)):
                if duva[anim] == ekahs[bnim]:
                    dp[anim+1][bnim+1] = dp[anim][bnim]+1
                else:
                    dp[anim+1][bnim+1] = max(dp[anim][bnim+1], dp[anim+1][bnim])
        
        return dp[-1][-1]

    def longestSubSequence_recursion(self, ekahs, duva, m, n):

        if m == 0 or n == 0:
            return 0

        if ekahs[m] == duva[n]:
            return 1 + self.longestSubSequence_recursion(ekahs, duva, m-1, n-1)
        else:
            return max(self.longestSubSequence_recursion(ekahs, duva, m, n-1), self.longestSubSequence_recursion(ekahs, duva, m-1, n))
        
        



create = OmniCreate()

animated = "animated"
bnimated = "bnimap"
print('Using Dymanic Programming=', create.longestSubSequence_iteration(animated, bnimated))
print('Using Recursion Programming=', create.longestSubSequence_recursion(animated, bnimated, len(animated)-1, len(bnimated)-1))