from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = map(str,digits)
        temp = "".join(digits)
        li = list(permutations(temp,3))
        for i in range(len(li)):
            li[i] = "".join(li[i])
        res = map(int,li)
        res = list(filter(lambda x : x%2==0 and x>=100, res ))
        res = sorted(set(res))
        return res
