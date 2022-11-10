class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = []

        for i in s:
            if ans and ans[-1] == i.swapcase():
                ans.pop()
            else:
                ans.append(i)

        return ''.join(ans)

            


inp = input()

s1 = Solution()
print(s1.makeGood(inp))