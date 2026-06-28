class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        di = {ch : i for i,ch in enumerate(order)}
        res = sorted(words,key= lambda word : [di.get(c,float('inf')) for c in word])
        return words == res