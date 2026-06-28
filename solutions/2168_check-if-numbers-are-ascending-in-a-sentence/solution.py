class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num_li = [int(num) for num in s.split() if num.isdigit()]
        return num_li == sorted(set(num_li))
        