# from itertools import permutations 

class Solution:
    def maxLength(self, arr):
        for i in range(len(arr)-1):
            dic = {}
            for k in range(26):
                dic[ord('a')+k] = 0
            for j in range(i+1,len(arr)):
                maxz+=1

        # realMax = 0
        # for i in range(len(arr)):
            
        #     perm = permutations(arr,i+1)
        #     for j in perm:
        #         dic = {}
        #         for k in range(26):
        #             dic[ord('a')+k] = 0
        #         strr = ""
        #         for k in j:
        #             strr+=k
        #         maxz = 0
        #         for k in strr:
        #             if dic[ord(k)] == 0:
        #                 dic[ord(k)] = 1
        #                 maxz+=1
        #                 # print(strr,end = ' ')
        #                 # print('this'+k,end=' ')
        #             else:
        #                 maxz = 0
        #                 break
                
        #         if realMax < maxz:
        #             realMax = maxz
        #         # print(realMax)
        # return realMax
        
            
        
                


inp = input().split(' ')
s1 = Solution()
print(s1.maxLength(inp))

