from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        res = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            res[key].append(string)
        return list(res.values())

        