class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        
        left, right = 0, 0
        string_set = set()
        longest = 0

        while right < len(s):
            if s[right] in string_set:
                string_set.remove(s[left])
                left += 1

            else:
                string_set.add(s[right])
                right += 1
                longest = max(longest, right - left)
        return longest

