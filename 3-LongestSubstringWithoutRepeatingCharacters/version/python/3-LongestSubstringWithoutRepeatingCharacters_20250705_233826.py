# Last updated: 7/5/2025, 11:38:26 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        r=0
        longest=0
        for i in s:
            while i in sett:
                sett.remove(s[l])
                l+=1
            w=(r-l+1)
            longest=max(longest,w)
            sett.add(i)
            r+=1
        return longest
