# Last updated: 6/14/2025, 10:32:50 PM
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1

        prev = 0
        cur = 1
        for i in range(2,n+1):
            prev,cur=cur,prev+cur

        return cur