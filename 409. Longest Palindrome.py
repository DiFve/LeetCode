from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        count = sorted(count.values(), reverse=True)
        ans = 0
        isOdd = False
        for i in count:
            if i%2==0:
                ans+=i
            else:
                ans+=i-1
                isOdd = True
        if isOdd:
            ans+=1
        return ans

        
inp = input()
s1 = Solution()
print(s1.longestPalindrome(inp))
