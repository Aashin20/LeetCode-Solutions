# Last updated: 6/14/2025, 10:32:23 PM
class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        c = 0
        n = len(pref)
        for word in words:
            if len(word) >= n and word[:n] == pref:
                c += 1
        return c