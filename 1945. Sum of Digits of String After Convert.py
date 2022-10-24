class Solution:
    def getLucky(self, s,k):
        numList = []
        sum = 0
        
        for i in s:
            if i>='A' and i<='Z':
                numList.append(int(ord(i)-ord('A')+1))
            if i>='a' and i<='z':
                numList.append(int(ord(i)-ord('a')+1))
        for i in numList():
            while i/10!= 0:
                sum+=(i%10)
                i/=10
            sum+=i
        
        for i in range(1,k):
            realSum = sum
            while sum/10 != 0:
                realSum += (sum%10)
                sum/=10
            
            

s = input()
k = int(input())

s1 = Solution()
s1.getLucky(s,k)