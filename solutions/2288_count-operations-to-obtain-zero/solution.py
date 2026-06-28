class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0 
        while(num1 and num2):
            if num1>num2:
                count += num1//num2
                num1 %= num2
            elif num2>num1:
                count += num2//num1
                num2 %= num1
            else:
                return count + 1
        return count