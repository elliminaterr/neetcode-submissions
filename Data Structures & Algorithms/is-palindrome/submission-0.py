
class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ""
        for x in s:
            if x.isalnum(): 
                out += x
        s = out.lower()

        p1 = 0
        p2 = len(s) - 1

        for i in range(len(s)//2):
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True

