class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for strings in words:
            strings = strings.replace(separator," ")
            strings = strings.strip()
            if strings.split(separator)!=[""]:
                res.extend(strings.split())
        return res