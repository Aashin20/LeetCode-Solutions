# Last updated: 3/8/2026, 11:15:23 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res = ""
4        res_len=0
5        for i in range(len(s)):
6            l,r=i,i
7            while l>=0 and r<len(s) and s[l]==s[r]:
8                if (r-l+1)>res_len:
9                    res_len = (r-l+1)
10                    res=s[l:r+1]
11                r+=1
12                l-=1
13        for i in range(len(s)):
14            l,r=i,i+1
15            while l>=0 and r<len(s) and s[l]==s[r]:
16                if (r-l+1)>res_len:
17                    res_len = (r-l+1)
18                    res=s[l:r+1]
19                r+=1
20                l-=1
21        return res