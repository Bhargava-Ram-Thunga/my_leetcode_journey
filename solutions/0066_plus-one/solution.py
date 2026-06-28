class Solution(object):
    def plusOne(self, digits):
        res = str(int("".join(str(n) for n in digits))+1)
        req = []
        for n in res:
            req.append(int(n))
        return req

        