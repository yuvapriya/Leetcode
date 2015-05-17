class Solution:
    # @return an integer
    def romanToInt(self, s):
        if len(s)==0:
            return 0
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result = 0
        i = 0
        while i < len(s):
            for r in range(len(roman)):
                if(len(roman[r]) == 1 and i<len(s) and s[i] == roman[r]):
                    result+=number[r]
                    i = i + 1
                elif(len(roman[r]) == 2 and i+1 < len(s) and s[i]+s[i+1] == roman[r]):
                    result+=number[r]
                    i = i + 2
        return result
s= Solution()
print s.romanToInt('MCMXCVI')
            
        