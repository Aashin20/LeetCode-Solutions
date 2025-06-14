# Last updated: 6/14/2025, 10:32:32 PM
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        for i in range(len(s)):
            s=s.replace(part,'',1)
            if part not in s:
                break
        return s