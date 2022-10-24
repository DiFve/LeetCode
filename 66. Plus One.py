

from unicodedata import digit


class Solution:
    def plusOne(self, digits):
        tod = 0
        digits[-1]+=1
        for i in range(1,len(digits)+1):
            # print(digits[-i])
            if(tod==1):
                digits[-i]+=1
                tod=0
            if(digits[-i]>=10):
                digits[-i] = 0
                tod = 1
        if tod == 1:
            digits.insert(0,1)
        return digits

s1 = Solution()
inp = [int(x) for x in input().split(' ')]
print(s1.plusOne(inp))