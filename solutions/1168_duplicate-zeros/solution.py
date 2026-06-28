class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        temp = arr.copy()
        i = 0
        while i < len(arr):
            if temp[i] == 0:
                temp.insert(i,0)
                i+=1
            i+=1
        arr[:] = temp[:len(arr)]
        