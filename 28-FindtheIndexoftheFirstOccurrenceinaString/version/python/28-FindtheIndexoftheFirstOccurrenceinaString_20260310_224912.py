# Last updated: 3/10/2026, 10:49:12 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if needle in haystack:
4            return haystack.index(needle)
5        return -1