class Solution:
    def romanToInt(self, s:str) ->int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        sp_romanDict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        end = 0

        for sp_roman in sp_romanDict:
            if sp_roman in s:
                end += sp_romanDict[sp_roman]
                s = s.replace(sp_roman,'')
        for i in s:
            if i in romanDict:
                end += romanDict[i]
        return end

sol = Solution()
print(sol.romanToInt('IXXX'))