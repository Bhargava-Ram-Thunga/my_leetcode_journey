class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        n = len(arr)
        c = int(n*0.05)
        arr = arr[c:n-c]
        return sum(arr)/len(arr)