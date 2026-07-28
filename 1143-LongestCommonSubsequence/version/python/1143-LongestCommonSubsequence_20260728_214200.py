# Last updated: 7/28/2026, 9:42:00 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m=len(text1)
4        n=len(text2)
5        dp={}
6        def longest(i,j):
7            if i==m or j==n: return 0
8            if (i,j) in dp: return dp[(i,j)]
9            if text1[i]==text2[j]:
10                return 1+longest(i+1,j+1)
11            else:
12                dp[(i,j)]=max(longest(i+1,j),longest(i,j+1))
13                return dp[(i,j)]
14        return longest(0,0)