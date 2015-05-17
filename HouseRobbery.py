#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if(len(num) == 0):
            return 0
        value1 = num[0]
        if(len(num) == 1):
            return value1
        value2 = max(num[0],num[1])
        if(len(num) == 2):
            return value2
        for i in range(2,len(num)):
            value = max(value2, value1 + num[i])
            value1 = value2
            value2 = value
        return value
   

s =Solution()
print s.rob([1,5,3,1,6])
print s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])