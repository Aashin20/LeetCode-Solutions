# Last updated: 7/23/2026, 2:45:34 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1=len(s1)
4        n2=len(s2)
5        if n1>n2: return False
6        s1_count=[0]*26
7        s2_count=[0]*26
8        for i in range(n1):
9            s1_count[ord(s1[i])-ord('a')]+=1
10            s2_count[ord(s2[i])-ord('a')]+=1
11        if s1_count==s2_count: return True
12        for i in range(n1,n2):
13            s2_count[ord(s2[i])-ord('a')]+=1
14            s2_count[ord(s2[i-n1])-ord('a')]-=1
15            if s2_count==s1_count: return True
16        return False
17            
18            