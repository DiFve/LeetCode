class Solution:
    def thousandSeparator(self, n: int) -> str:
        nStr = str(n)
        if len(nStr) <= 3:
            return nStr
        temp = len(nStr)%3
        if temp == 0:
            temp = 3
        ans = nStr[:temp]
        ans+='.'
        for i in range(temp,len(nStr),3):
            ans+=nStr[i]
            ans+=nStr[i+1]
            ans+=nStr[i+2]
            ans+='.'
        ans = ans[:-1]
        return ans
        print(ans)
inp = int(input())
Solution().thousandSeparator(inp)
