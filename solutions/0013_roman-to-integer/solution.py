class Solution(object):
    def romanToInt(self, s):
        num = 0
        s=s.replace("IV","IIII")
        s=s.replace("IX","IIIIIIIII")
        s=s.replace("CD","CCCC")
        s=s.replace("XC","XXXXXXXXX")
        s=s.replace("XL","XXXX")
        s=s.replace("CM","CCCCCCCCC")
        for c in s:
            if c=="M":
                num+=1000
            elif c=="D":
                num+=500
            elif c=="C":
                num+=100
            elif c=="L":
                num+=50
            elif c=="X":
                num+=10
            elif c=="V":
                num+=5
            elif c=="I":
                num+=1
        return num