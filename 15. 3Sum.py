class Solution:
    def threeSum(self, nums) :
        mySet = set()
        for i in range (0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if(i!=j!=k and nums[i]+nums[j]+nums[k]==0):
                        lst = [nums[i],nums[j],nums[k]]
                        lst.sort()
                        mySet.add(tuple(lst))
        # print(list(mySet))
        return list(mySet)




inp = [int(x) for x in input().split(',')]
s1 = Solution()

s1.threeSum(inp)
