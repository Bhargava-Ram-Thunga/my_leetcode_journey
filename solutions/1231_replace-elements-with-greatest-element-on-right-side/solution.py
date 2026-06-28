class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[-1]
        res = [-1]
        for i in range(-1,-len(arr),-1):
            if arr[i] >= temp:
                res.append(arr[i])
                temp = arr[i]
            else:
                res.append(temp)
        return res[::-1]