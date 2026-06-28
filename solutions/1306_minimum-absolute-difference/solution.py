class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        ns = set(arr)
        temp = [arr[i+1]- arr[i] for i in range(len(arr)-1)]
        temp.append(arr[-1]-arr[-2])
        temp = min(temp)
        res = []
        for num in ns:
            if num + temp in ns:
                res.append([num,num+temp])
        return sorted(res)