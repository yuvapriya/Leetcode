class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if(n == 0):
            return 0
        last = 1
        lastButOne = 0
        for i in range(1,n+1):
            newL = last + lastButOne
            lastButOne = last
            last = newL
        return last