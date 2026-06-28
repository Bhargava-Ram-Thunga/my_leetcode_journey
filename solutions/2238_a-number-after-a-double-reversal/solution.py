class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        temp = int(str(int(str(num)[::-1]))[::-1])
        return temp == num