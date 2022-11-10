class Solution:
    def findDuplicate(self, nums):
        temp = []
        for i in nums:
            if i in temp:
                return i
            temp.append(i)

inp = [int(x) for x in input().split(' ')]
Solution().findDuplicate(inp)