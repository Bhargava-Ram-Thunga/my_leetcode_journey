def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        li = []
        res = []
        for i in range(len(nums)):
            li.append(nums[i][i])
            li.append(nums[i][len(nums)-i-1])
        for num in li:
            if isPrime(num):
                res.append(num)
        if res:
            return max(res)
        return 0
        