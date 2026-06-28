class Solution(object):
    def countDigits(self, num):
        count = 0
        for c in str(num):
            if num%int(c)==0:
                count+=1
        return count
        