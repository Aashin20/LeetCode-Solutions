# Last updated: 9/9/2025, 6:13:09 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sett = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = r-l+1
            longest = max(w,longest)
            sett.add(s[r])
        return longest
            
