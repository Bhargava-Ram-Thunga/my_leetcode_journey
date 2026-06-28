class Solution(object):
    def maximum69Number (self, num):
        res = ""
        flag = True
        for c in str(num):
            if c=="6" and flag:
                res+="9"
                flag=False
            else:
                res+=c
        return int(res)