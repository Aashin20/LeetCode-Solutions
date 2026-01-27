# Last updated: 1/27/2026, 8:59:55 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n==0:
4            return 0
5        if n==1:
6            return 1
7        prev=1
8        cur=2
9        for i in range(3,n+1):
10            prev,cur=cur,prev+cur
11        return cur