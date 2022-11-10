class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openParam = 0
        closrParam = 0
        for i in s:
            if i == '(':
                openParam+=1
            elif i == ')':
                if openParam>0:
                    openParam-=1
                else:
                    closrParam+=1
        return openParam+closrParam


inp = input()
Solution().minAddToMakeValid(inp)