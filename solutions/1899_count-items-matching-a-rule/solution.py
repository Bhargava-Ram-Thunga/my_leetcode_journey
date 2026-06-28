class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            search_ind = 0
        elif ruleKey == "color":
            search_ind = 1
        elif ruleKey == "name":
            search_ind = 2
        for li in items:
            if li[search_ind]==ruleValue:
                count+=1
        return count