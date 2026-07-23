# Last updated: 7/23/2026, 1:18:44 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        L=0
4        sett=set()
5        n=len(s)
6        longest=0
7        for R in range(len(s)):
8            while s[R] in sett:
9                sett.remove(s[L])
10                L+=1
11            sett.add(s[R])
12            longest=max(longest,(R-L)+1)
13        return longest
14            
15