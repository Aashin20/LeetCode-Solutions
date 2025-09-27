# Last updated: 9/27/2025, 9:04:56 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)
        if ss==tt:
            return True
        else:
            return False