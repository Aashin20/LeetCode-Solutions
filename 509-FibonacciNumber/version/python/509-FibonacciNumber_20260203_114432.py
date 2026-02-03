# Last updated: 2/3/2026, 11:44:32 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n==0:
4            return 0
5        if n==1:
6            return 1
7        prev = 0
8        cur = 1
9        for i in range(2,n+1):
10            prev,cur=cur,prev+cur
11        return cur