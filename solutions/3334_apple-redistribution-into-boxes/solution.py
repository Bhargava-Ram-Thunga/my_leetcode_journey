class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        for i in range(len(capacity)):
            if total_apples <= capacity[i]:
                print(capacity)
                return i+1
            else:
                total_apples -= capacity[i]
        return i+1
                