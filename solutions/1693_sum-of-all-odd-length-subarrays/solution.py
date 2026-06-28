class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr)%2:
            res = sum(arr)
        else:
            res = 0
        for i in range(1,len(arr),2):
            for j in range(len(arr)+1):
                if j+i <len(arr)+1:
                    res += sum(arr[j:j+i])
        return res