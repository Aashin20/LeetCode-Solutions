# Last updated: 8/17/2026, 1:47:32 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        L=0
4        sett = set()
5        count=0
6        ans=0
7        for R in range(len(s)):
8            if s[R] in sett:
9                ans=max(ans,count)
10                while s[R] in sett:
11                    sett.remove(s[L])
12                    L+=1
13                    count-=1
14            sett.add(s[R])
15            count+=1
16        return max(count,ans)
17