# Last updated: 6/14/2025, 10:33:27 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=Counter(s)
        b=Counter(t)
        return a==b