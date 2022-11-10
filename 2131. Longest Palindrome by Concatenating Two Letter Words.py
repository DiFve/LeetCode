from collections import Counter

class Solution:
    def longestPalindrome(self, words):
        ans = 0
        count = Counter(words)
        isCenter = False
        for i,j in count.items():
            
            if(i[0]==i[1]):
                if(j%2 == 0):
                    ans+=j
                else:
                    isCenter = True
                    ans += j-1
            elif(i[0]<i[1]):
                ans+=2*min(j,count[i[1]+i[0]])
        if isCenter:
            ans+=1
        return ans*2


inp = input().split(' ')
s1 = Solution()
print(s1.longestPalindrome(inp))

        