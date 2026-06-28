class Solution:
    def minimumSum(self, num: int) -> int:
        temp = sorted(str(num))[::-1]
        temp = "".join(temp)
        temp = list(temp.strip())
        l = len(temp)
        l1 = ""
        l2 = ""
        for i in range((l//2)+1):
            if not temp:
                break
            else:
                l1+=temp.pop()
                l2+=temp.pop()
        return int(l1)+int(l2)
        
        
        