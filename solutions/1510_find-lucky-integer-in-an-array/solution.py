class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr = sorted(arr,reverse = True)
        for num in arr:
            if arr.count(num) == num :
                return num
        return -1