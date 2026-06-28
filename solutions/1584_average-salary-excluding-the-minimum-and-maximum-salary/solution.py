class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        res = (sum(salary)-max(salary)-min(salary))
        return res/(n-2)