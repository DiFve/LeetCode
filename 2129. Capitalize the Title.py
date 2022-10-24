class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        newString = ""
        for i, subString in enumerate(title): 
            if len(subString) == 1 or len(subString) == 2:
                newString+=(subString.lower())
            else:
                upperString = subString[0].upper() + subString[1:].lower()
                newString+=(upperString)
            if i != len(title)-1:
                newString += " " 
        return newString



string = input()
s1 = Solution()
print(s1.capitalizeTitle(string))

# print(s1.capitalizeTitle(string))
