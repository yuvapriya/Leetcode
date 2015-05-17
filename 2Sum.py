class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d and d[key]!=i:
                mi = min(d[key],i)
                ma = max(d[key],i)
                return [mi + 1, ma + 1]
        return []