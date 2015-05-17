class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if(len(nums)<2):
            return []
        result = []
        nums.sort()
        for i in range(0,len(nums)-2):
            l = i+1 # first element in the rest of the array
            r = len(nums) - 1 # last
            while l < r:
                if ( nums[i] + nums[l] + nums[r] == 0):
                    if [nums[i] , nums[l] , nums[r]] not in result:
                        result.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                else:
                    if ( nums[i] + nums[l] + nums[r] < 0):
                        l+=1
                    else:
                        r-=1
        return result