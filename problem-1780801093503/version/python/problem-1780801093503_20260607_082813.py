# Last updated: 6/7/2026, 8:28:13 AM
1class Solution:
2    def sumOfGoodIntegers(self, n: int, k: int) -> int:
3        ans=0
4        for i in range(max(1,n-k),n+k+1):
5            if (n&i)==0:
6                ans+=i
7        return ans