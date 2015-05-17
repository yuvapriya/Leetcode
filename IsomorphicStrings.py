class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds = self.buildDict(s)
        dt = self.buildDict(t)
        for key in ds:
            vals = ds[key]
            found = 0
            for key2 in dt:
                if dt[key2] == vals:
                    found = 1
                    break
            if found == 0:
                return False
        return True
                        
    def buildDict(self, s):
        d= {}
        for i in range(len(s)):
            ch = s[i]
            if ch in d.keys():
                d[ch].append(i)
            else:
                d[ch] = [i]
        return d