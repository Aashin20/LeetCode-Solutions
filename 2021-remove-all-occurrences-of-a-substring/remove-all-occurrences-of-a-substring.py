class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        for i in range(len(s)):
            s=s.replace(part,'',1)
            if part not in s:
                break
        return s