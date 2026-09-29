# Last updated: 9/29/2026, 11:32:01 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        L=0
4        sett=set()
5        longest=0
6        for R in range(len(s)):
7            while s[R] in sett:
8                sett.remove(s[L])
9                L+=1
10            sett.add(s[R])
11            longest=max(longest,(R-L)+1)
12        return longest