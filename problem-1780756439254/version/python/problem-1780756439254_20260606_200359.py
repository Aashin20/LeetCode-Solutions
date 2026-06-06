# Last updated: 6/6/2026, 8:03:59 PM
1class Solution:
2    def consecutiveSetBits(self, n: int) -> bool:
3        b=bin(n)[2:]
4        count=0
5        for i in range(len(b)-1):
6            if b[i:i+2]=='11':
7                count+=1
8        return count==1