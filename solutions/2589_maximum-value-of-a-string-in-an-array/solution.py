class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for i in range(len(strs)):
            if strs[i].isdigit():
                res.append(int(strs[i]))
            else:
                res.append(len(strs[i]))
        return max(res)
