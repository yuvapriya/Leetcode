#Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#For example:
#Given the following binary tree,

#   1            <---
# /   \
#2     3         <---
# \     \
#  5     4       <---

#You should return [1, 3, 4]. 
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root == None:
            return []
        queue = []
        result = []
        queue.append(root)
        while (len(queue) !=0):
            currLevel = queue
            queue = []
            for i in range(len(currLevel)):
                node = currLevel[i]
                 # last node
                if (i == len(currLevel)-1):
                    result.append(node.val)
                if(node.left != None):
                    queue.append(node.left)
                if(node.right != None):
                    queue.append(node.right)
        return result
        
one =TreeNode(1)
one.left = TreeNode(2)
one.left.right = TreeNode(5)
one.right = TreeNode(3)
one.right.right = TreeNode(4)
s = Solution()
print s.rightSideView(one)