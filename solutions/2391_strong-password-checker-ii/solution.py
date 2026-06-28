class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) <8:
            return False
        l_char = set('abcdefghijklmnopqrstuvwxyz')
        u_char = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sym = set('!@#$%^&*()-+')
        nums = set('0123456789')
        setChar = set(password)
        for c in setChar:
            if c*2 in password:
                return False
        if setChar & l_char and setChar & u_char and setChar & sym and setChar & nums:
            return True
        return False
        
        
