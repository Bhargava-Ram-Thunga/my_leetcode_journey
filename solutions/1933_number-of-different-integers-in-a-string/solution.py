import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = re.findall(r'\d+',word)
        nums = list(map(int,nums))
        return len(set(nums))
        