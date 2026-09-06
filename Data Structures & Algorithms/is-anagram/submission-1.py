class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        character_counter = [0]*26

        for i in range(len(s)):
            character_counter[ord(s[i])-97] += 1
            character_counter[ord(t[i])-97] -= 1

        if character_counter == [0]*26:
            return True
        else:
            return False
        