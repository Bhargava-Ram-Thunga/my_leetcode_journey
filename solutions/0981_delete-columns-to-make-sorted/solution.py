class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([sorted(col) != col for col in map(list,zip(*strs))])

            
