from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        maxz = -1
        isOdd = False
        lstNum = []
        lstCount = []
        ans = ""
        for i in sorted(count.keys(),reverse=True):
            if count[i] % 2 == 0:
                lstNum.append(i)
                lstCount.append(count[i])
            else:
                if(count[i] >1):
                    lstNum.append(i)
                    lstCount.append(count[i]-1)
                if(int(i) > maxz):
                    maxz = int(i)
                    isOdd = True
        
        for i in range(len(lstNum)):
            if(lstNum[i]=='0' and ans==""):
                continue
            ans+=lstNum[i]*int((int(lstCount[i])/2))
        if(not isOdd and ans==""):
            return str(0)
        if isOdd:
            ans+=str(maxz)
            ans+=ans[-2::-1]
            return ans
        return ans+ans[::-1]

 
inp = input()
s1 = Solution()
print(s1.largestPalindromic(inp)  )      