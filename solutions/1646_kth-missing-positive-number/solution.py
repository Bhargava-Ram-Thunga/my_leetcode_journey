class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = []
        i=1
        while len(res)<k+1:
            if i not in arr:
                res.append(i)
            i+=1
        return res[k-1]