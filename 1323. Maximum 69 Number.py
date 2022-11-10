class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        if '6' not in numStr:
            return num
        x = numStr.index('6')
        
        ans = ""
        ans+=numStr[:x]
        ans+='9'
        ans+=numStr[x+1:]
        return int(ans)
            

        
inp = int(input())
s1 = Solution()
print(s1.maximum69Number(inp))
