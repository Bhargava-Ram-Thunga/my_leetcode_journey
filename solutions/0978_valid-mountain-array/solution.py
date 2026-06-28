class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) <3) or (arr[0] >= arr[1]) or (arr[-1] >= arr[-2]):
            return False
        dec = False
        for i in range(1,len(arr)):
            if (arr[i-1] == arr[i]) or (dec and arr[i-1] <= arr[i]) :
                return False
            elif not(dec) and arr[i-1] > arr[i]:
                dec = True
        return True
