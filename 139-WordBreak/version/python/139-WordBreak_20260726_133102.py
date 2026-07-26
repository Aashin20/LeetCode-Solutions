# Last updated: 7/26/2026, 1:31:02 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        dp=[False]*(len(s)+1)
4        dp[len(s)]=True
5        for i in range(len(s)-1,-1,-1):
6            for w in wordDict:
7                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
8                    dp[i]=dp[i+len(w)]
9                if dp[i]:
10                    break
11        return dp[0]