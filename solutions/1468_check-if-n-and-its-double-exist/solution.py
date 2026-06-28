class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if 0 in arr and arr.count(0)>1:
            return True
        for num in arr:
            if num*2 in arr and arr.index(num) != arr.index(2*num):
                return True   
        return False