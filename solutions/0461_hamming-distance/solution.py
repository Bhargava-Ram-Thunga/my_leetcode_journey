class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
            x_bin = bin(x)[2:]
            y_bin = bin(y)[2:]
            l = max(len(x_bin),len(y_bin))
            x_bin = "0"*(l-len(x_bin))+x_bin
            y_bin = "0"*(l-len(y_bin))+y_bin
            count = 0
            for i in range(l):
                if x_bin[i]!=y_bin[i]:
                    count+=1
            return count
            