class Solution:
    def intToRoman(self, num: int) -> str:
        dif = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        val = list(map(int,list(str(num))))[::-1]
        for i in range(len(val)):
            val[i] = val[i]*(10**i)
        val = val[::-1]
        for i in range(len(val)):
            if val[i] in dif:
                val[i] = dif[val[i]]
        val = val[::-1]
        for i in range(len(val)):
            if isinstance(val[i],int):
                num = val[i]
                temp = (10**i)*5
                if num > temp:
                    l = (num-temp)//(10**i)
                    val[i] = dif[temp] + (dif[10**i])*l
                else:
                    l = num//(10**i)
                    val[i] = (dif[10**i])*l
        val = val[::-1]
        return "".join(val)
