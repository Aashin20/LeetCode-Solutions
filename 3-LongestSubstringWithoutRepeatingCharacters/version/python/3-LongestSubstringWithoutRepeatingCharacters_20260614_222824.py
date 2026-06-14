# Last updated: 6/14/2026, 10:28:24 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l=0
4        sett = set()
5        longest = 0
6        for r in range(len(s)):
7            while s[r] in sett:
8                sett.remove(s[l])
9                l+=1
10            w = r-l+1
11            longest = max(w,longest)
12            sett.add(s[r])
13        return longest
14            
15