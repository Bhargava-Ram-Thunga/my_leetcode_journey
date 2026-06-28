class Solution:
    def generateTag(self, caption: str) -> str:
        
        return "#" + (((caption.split())[0]).lower()+"".join(list(map(lambda x : x.title(),(caption.split()[1:])))))[:99] if caption.split() else "#"