def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left,right+1):
            n = (bin(i)[2:]).count("1")
            if isPrime(n) and n!=1:
                count+=1
        return count
        