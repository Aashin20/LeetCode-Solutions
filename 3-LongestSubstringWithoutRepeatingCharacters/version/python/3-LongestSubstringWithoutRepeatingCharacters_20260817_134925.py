# Last updated: 8/17/2026, 1:49:25 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        L=0
4        sett = set()
5        count=0
6        ans=0
7        for R in range(len(s)):
8            if s[R] in sett:
9                while s[R] in sett:
10                    sett.remove(s[L])
11                    L+=1
12                    count-=1
13            sett.add(s[R])
14            count+=1
15            ans=max(count,ans)
16        return ans
17