class Solution:
    def myAtoi(self, s: str) -> int:
        if(s.isdigit()):
            if(int(s)>(2**31) - 1):
                return (2**31) - 1
            elif (int(s)<-(2**31)):
                return (-(2**31))
            else:
                return int(s)
        if(s=="+" or s=="-"):
            return 0
        s = s.strip()

        for i in range(len(s)-1):
            if((s[i]=="+" or s[i]=="-") and not(s[i+1].isdigit())):
                return 0
            if(s[i].isdigit() and not(s[i+1].isdigit())):
                s = s[:i+1]
                break
            if(s[i] not in "+-" and not(s[i].isdigit())):
                s = s[:i]
                break

        if(len(s)>0):
            if(int(s)>(2**31) - 1):
                return (2**31) - 1
            elif (int(s)<-(2**31)):
                return (-(2**31))
            else:
                return int(s)
        return 0

        
            

            
            
