class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelBackList = []
        for i in range(len(s)-1,-1,-1):
            if s[i] in 'aeiouAEIOU':
                vowelBackList.append(s[i])
                count = 0
        ans = ""
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                ans += vowelBackList[count]
                count+=1
            else:
                ans+=s[i]
        return ans

inp = input()
# print(Solution().reverseVowels(inp))
s1 = Solution()
print(s1.reverseVowels(inp))
