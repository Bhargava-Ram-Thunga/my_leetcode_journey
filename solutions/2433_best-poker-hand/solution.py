from collections import Counter as cs
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # flush > three > pair > high 
        ranks_count = dict(cs(ranks))
        ranks_val = ranks_count.values()
        suits_set = set(suits)
        if len(suits_set) ==1:
            return "Flush"
        elif 3 in ranks_val or 4 in ranks_val:
            return "Three of a Kind"
        elif 2 in ranks_val:
            return "Pair"
        return "High Card"
