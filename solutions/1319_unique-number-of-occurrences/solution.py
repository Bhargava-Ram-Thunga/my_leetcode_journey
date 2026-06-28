class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = sorted(set(arr))
        count_li = []
        for num in s:
            count_li.append(arr.count(num))
        return len(set(count_li)) == len(count_li)
