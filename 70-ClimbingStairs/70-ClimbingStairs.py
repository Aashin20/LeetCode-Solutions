# Last updated: 6/14/2025, 10:34:03 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        prev=1
        cur=2
        for i in range(3,n+1):
            prev,cur=cur,prev+cur
        return cur
        