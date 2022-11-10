class Solution:
    def minimumTotal(self, triangle) -> int:
        cloneTri = [[-1] * i for i in range(1,len(triangle)+1)]
        cloneTri[-1] = triangle[-1]
        # print(cloneTri)
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                temp1 = triangle[i][j] + cloneTri[i+1][j]
                temp2 = triangle[i][j] + cloneTri[i+1][j+1]
                cloneTri[i][j] = min(temp1,temp2)
        return cloneTri[0][0]

tri = []
for i in range(1,5):
    lst = []
    for j in range(i):
        inp = int(input())
        lst.append(inp)
    tri.append(lst)

s1 = Solution()
s1.minimumTotal(tri)