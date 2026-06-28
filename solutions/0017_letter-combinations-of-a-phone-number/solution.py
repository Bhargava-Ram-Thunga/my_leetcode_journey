from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        al = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        li = []
        for digit in digits:
            li.append(al[int(digit)])
        # print(li)
        res = [''.join(p) for p in product(*li)]
        return res