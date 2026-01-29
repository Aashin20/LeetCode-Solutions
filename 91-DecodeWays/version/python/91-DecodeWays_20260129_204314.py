# Last updated: 1/29/2026, 8:43:14 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        dp = {len(s):1}
4        for i in range(len(s)-1,-1,-1):
5            if s[i] == '0':
6                dp[i]=0
7            else:
8                dp[i]=dp[i+1]
9            if(i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
10                dp[i]+=dp[i+2]
11        return dp[0]