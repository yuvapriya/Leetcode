class Solution:
    def rotate(self, nums, k):
        l = len(nums)
        if(l == 0 or k%l <= 0):
            return
        rev = self.reverse(nums, 0 , l-1)
        rev = self.reverse(rev, 0, k-1)
        rev = self.reverse(rev, k, l-1)
        return rev
       # rotation = k % l
    #    index = l - rotation
    #    return nums[index:]+nums[0:index]
        
    def reverse(self, input, start, end):
        str = list(input)
        while(start < end):
            str[start],str[end] = str[end],str[start]
            start+=1
            end-=1
        return str

s = Solution()
print s.rotate([1,2],1)