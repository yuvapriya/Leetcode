# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if ( root == None):
            return 0
        if(root.left == None and root.right == None):
            return 1
        lDepth = self.minDepth(root.left)
        rDepth = self.minDepth(root.right)
        if(lDepth == 0):
            lowest = rDepth
        elif(rDepth == 0):
            lowest = lDepth
        else:
            lowest = min(lDepth, rDepth)
        return 1+ lowest