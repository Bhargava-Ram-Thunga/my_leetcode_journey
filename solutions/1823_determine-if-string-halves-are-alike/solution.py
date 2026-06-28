class Solution(object):
    def halvesAreAlike(self, s):
        vowels = "AEIOUaeiou"
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if i>((len(s)/2)-1) and (s[i] in vowels):
                count2+=1
            if i<=((len(s)/2)-1) and (s[i] in vowels):
                count1+=1
        if count1==count2:
            return True
        return False
                
        