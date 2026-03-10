# Last updated: 3/10/2026, 12:06:36 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
4        n = len(s)
5        i = 0
6        summ = 0
7        while i<n:
8            if i<n-1 and d[s[i]]<d[s[i+1]]:
9                summ += d[s[i+1]]-d[s[i]]
10                i+=2
11            else:
12                summ+=d[s[i]]
13                i+=1
14        return summ