class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [pivot]*nums.count(pivot)
        temp = 0
        for num in nums:
            if num>pivot:
                res.append(num)
            elif num<pivot:
                res.insert(temp,num)
                temp+=1
        return res