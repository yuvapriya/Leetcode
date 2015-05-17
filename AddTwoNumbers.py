#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if (l1 == None and l2 == None):
            return
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        result = ListNode(0)
        curr1 = l1
        curr2 = l2
        currResult = result
        carry = 0
        while(curr1 != None and curr2!=None):
            val = curr1.val + curr2.val + carry
            if val >= 10:
                carry = 1
            else:
                carry = 0
            currResult.next = ListNode(val % 10)
            currResult = currResult.next
            curr1 = curr1.next
            curr2 = curr2.next            
        while (curr1!=None):
            val = curr1.val + carry
            if val >= 10:
                carry = 1
            else:
                carry = 0
            currResult.next = ListNode(val % 10)
            currResult = currResult.next
            curr1 = curr1.next            
        while (curr2!=None):
            val = curr2.val + carry
            if val >= 10:
                carry = 1
            else:
                carry = 0
            currResult.next = ListNode(val % 10)
            currResult = currResult.next
            curr2 = curr2.next 
        if (carry >0):
            currResult.next = ListNode(carry)    
        return result.next
l1 = ListNode(5)
l2 = ListNode(5)
s = Solution()
res = s.addTwoNumbers(l1,l2)
curr = res
while(curr!=None):
    print curr.val
    curr = curr.next