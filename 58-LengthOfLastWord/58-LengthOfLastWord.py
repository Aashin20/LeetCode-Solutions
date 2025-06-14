# Last updated: 6/14/2025, 10:34:06 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        return len(a[-1])