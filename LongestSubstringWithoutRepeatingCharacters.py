"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1."""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use a moving window
        max_so_far = 0
        start = 0
        d = {}
        for i in range(len(s)):
            if(s[i] in d):
                start = max(start,d[s[i]]) # We have seen the character before so should the start change
            max_so_far = max(max_so_far, i-start+1) # Keep checking if adding this character improves the max
            d[s[i]] = i + 1
        return max_so_far
