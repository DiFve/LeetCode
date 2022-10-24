class Solution:
    def rearrangeCharacters(self, s,target):
        sDict = {}
        targetDict = {}
        for i in target:
            targetDict[i] = target.count(i)
        for i in target:
            sDict[i] = int((s.count(i)/targetDict[i]))
        return min(sDict.values())

            

