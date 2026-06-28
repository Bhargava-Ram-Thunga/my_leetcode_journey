class Solution:
    def isValid(self, s: str) -> bool:
        temp = int(len(s)/2)
        for i in range(temp):
            s = s.replace("()","")
            s = s.replace("{}","")
            s = s.replace("[]","")
        if s=="":
            return True
        return False