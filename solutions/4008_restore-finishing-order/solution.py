class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [f for f in order if f in friends]