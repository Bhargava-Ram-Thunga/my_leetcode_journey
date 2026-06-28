class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num in arr1:
            if not any(x in arr2 for x in range(num-d,num+d+1)):
                count +=1
        return count