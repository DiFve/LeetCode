

class Solution:
    def countCharacters(self, words, chars) :
        dictChars = {}
        for i in chars:
            dictChars[i] = chars.count(i)
        dictCharsTemp = dictChars
        count = 0
        countTemp = 0
        for i in words:
            dictCharsTemp = dictChars.copy()
            for j in i:
                if j not in chars:
                    countTemp = count
                    break
                if dictCharsTemp[j] > 0:
                    countTemp+=1
                    dictCharsTemp[j]-=1
                else:
                    countTemp = count
                    break
            
            
            count = countTemp
        return count

inp = input().split(' ')
inp2 = input()
s1 = Solution()

print(s1.countCharacters(inp,inp2))