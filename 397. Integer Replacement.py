import math

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n%2==0:
            return math.ceil(math.log(n,2))
        else:
            if(n==1):
                return 0
            return math.ceil(math.log(n-1,2))+1

inp = int(input())

print(Solution().integerReplacement(inp))