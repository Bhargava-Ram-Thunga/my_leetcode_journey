class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        temp = money
        money -= min(prices)
        prices.remove(min(prices))
        money -= min(prices)
        return money if money>=0 else temp