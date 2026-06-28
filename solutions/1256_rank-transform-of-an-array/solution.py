class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = sorted(set(arr))
        res = dict((num,i+1)for i,num in enumerate(res))
        ans = []
        for i in range(len(arr)):
            arr[i] = res[arr[i]]
        return arr