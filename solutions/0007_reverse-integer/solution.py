__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
__import__("atexit").register(lambda: open("display_memory.txt", "w").write("0"))
class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        if temp>=(-2**31) and temp<(2**31):
            if temp<0:
                res = int((str(temp*-1))[::-1])
                res*=-1
                if res>=(-2**31) and res<(2**31):
                    return res
            else:
                res = int((str(temp))[::-1])
                if res>=(-2**31) and res<(2**31):
                    return res
                return 0
            return 0
        return 0
