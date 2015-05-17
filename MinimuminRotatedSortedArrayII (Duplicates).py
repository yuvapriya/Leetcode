class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if (len(nums) == 0 ):
            return
        if(len(nums) == 1):
            return nums[0]
        return self.findMinR(nums, 0, len(nums) - 1)
    def findMinR(self, arr, low, high):
        if(high < low):
            return arr[0]
        if(high == low):
            return arr[low]
        mid = low + (high - low) / 2
        if mid < high and arr[mid + 1] < arr[mid]:
            return arr[mid+1]
        if mid > low and arr[mid] < arr[mid - 1]:
            return arr[mid]
        leftMin = self.findMinR(arr, low, mid-1)
        rightMin = self.findMinR(arr, mid+1, high)
        return min(leftMin, rightMin)