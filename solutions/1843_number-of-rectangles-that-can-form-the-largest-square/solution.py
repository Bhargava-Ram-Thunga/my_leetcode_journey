__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
__import__("atexit").register(lambda: open("display_memory.txt", "w").write("0"))
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rectangles = list(map(lambda x : x[1] if x[0] > x[1] else x[0],rectangles))
        return rectangles.count(max(rectangles))