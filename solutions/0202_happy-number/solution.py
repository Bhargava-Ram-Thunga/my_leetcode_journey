class Solution:
    def isHappy(self, n: int) -> bool:
        # n(int) -> string -> list -> map int(sqr)-> sum() ->
        li = []
        while True:
            tempLi = list(map(lambda x :int(x)**2,list(str(n))))
            n = sum(tempLi)
            if n in li:
                break
            li.append(n)
        # return li
        return n == 1