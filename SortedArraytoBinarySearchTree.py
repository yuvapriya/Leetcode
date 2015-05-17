# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if(len(num)==0):
            return
        if(len(num)==1):
            return TreeNode(num[0])
        return self.sortedArrayToBSTRecur(0,len(num) - 1, num)
        
    def sortedArrayToBSTRecur(self, low, high, num):
        if(high < low):
            return
        if(high == low):
            return TreeNode(num[high])
        mid = (low + high)/2
        r = TreeNode(num[mid])
        r.left = self.sortedArrayToBSTRecur(low, mid - 1, num)
        r.right = self.sortedArrayToBSTRecur(mid + 1, high, num)
        return r