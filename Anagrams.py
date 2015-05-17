#Given an array of strings, return all groups of strings that are anagrams.

#Note: All inputs will be in lower-case.
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anag = {}
        result = []
        for str in strs:
            s = ''.join(sorted(str))
            if (s in anag):
                anag[s].append(str)
            else:
                anag[s] = [str]
        for str in anag:
            if(len(anag[str])>1):
                result = result + anag[str]
        return result
    