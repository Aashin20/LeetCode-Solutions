# Last updated: 7/28/2026, 9:17:33 AM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m=len(text1)
4        n=len(text2)
5        memo={}
6        def longest(i,j):
7            if (i,j) in memo:
8                return memo[(i,j)]
9            elif i==m or j==n:
10                return 0
11            elif text1[i]==text2[j]:
12                memo[(i,j)]= 1+longest(i+1,j+1)
13            else:
14                memo[(i,j)] = max(longest(i,j+1),longest(i+1,j))
15            return memo[(i,j)]
16        return longest(0,0)