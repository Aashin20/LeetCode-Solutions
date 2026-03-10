# Last updated: 3/10/2026, 11:31:40 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False 
5        ss = Counter(s)
6        tt = Counter(t)
7        return ss==tt