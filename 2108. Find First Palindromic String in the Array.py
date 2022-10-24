class Solution:
    def firstPalindrome(self, words) -> str:
        for subString in words:
            sum = 0
            for n in range(0,int(len(subString)/2)):
                # print(subString[n]+" "+subString[-(n+1)])
                if subString[n] == subString[-(n+1)]:
                    
                    sum+=1
                    continue
                else:
                    break
            if sum == int(len(subString)/2):
                return subString
        return ""



string = input().split()
s1 = Solution()
print(s1.firstPalindrome(string))