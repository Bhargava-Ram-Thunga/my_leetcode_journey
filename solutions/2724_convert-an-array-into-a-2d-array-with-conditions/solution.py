class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        temp = dict()
        res = []
        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num]=1
            if temp[num]-1 >= len(res):
                res.append([num])
            else:
                res[temp[num]-1].append(num)
        return res
            
