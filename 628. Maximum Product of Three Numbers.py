from numpy import ma


class Solution:
    def maximumProduct(self, nums) :
        nums.sort()

        ans1 = nums[-1]*nums[-2]*nums[-3]
        ans2 = nums[0]*nums[1]*nums[-1]

        return  max(ans1,ans2)
            

inp = [int(x) for x in input().split(' ')]
s1 = Solution()
print(s1.maximumProduct(inp))
