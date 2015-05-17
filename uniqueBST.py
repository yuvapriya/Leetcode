class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if(n<2):
            return 1
        sol = {}
        sol[0] = 1
        sol[1] = 1
        for i in range(2,n+1):
            sum = 0
            for j in range(1,i+1):
                sum = sum + (sol[j-1] * sol [i-j])
            sol[i] = sum
        return sol[n]
s = Solution()
print s.numTrees(4)