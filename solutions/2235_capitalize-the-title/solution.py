class Solution:
    def capitalizeTitle(self, titles: str) -> str:
        titles = titles.split()
        res = []
        for title in titles:
            if len(title)<=2:
                res.append(title.lower())
            else:
                res.append(title[0].upper()+title[1:].lower())
        return " ".join(res)