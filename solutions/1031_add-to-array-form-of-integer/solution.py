class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        k = list(map(int,list(str(k))[::-1]))
        i =0
        l = len(num)
        while(k):
            if i < l:
                num[i]+= k[0]
                i+=1
            else:
                num += [k[0]]
            k.pop(0)
        for i in range(len(num)):
            temp = num[i]//10
            num[i] %=10
            if(i<len(num)-1):
                num[i+1] += temp
            elif (i == len(num)-1 and temp):
                num.append(temp)
        return num[::-1]