# Last updated: 2/3/2026, 11:44:03 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n==0:
4            return 0
5        if n==1:
6            return 1
7
8        prev = 0
9        cur = 1
10        for i in range(2,n+1):
11            prev,cur=cur,prev+cur
12
13        return cur