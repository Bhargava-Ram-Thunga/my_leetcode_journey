class Solution(object):
    def isFascinating(self, n):
        temp = str(n)+str(n*2)+str(n*3)
        for i in range(1,10):
            if temp.count(str(i))>1 or (str(i) not in temp):
                return False
        return True
        