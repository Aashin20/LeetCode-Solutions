# Last updated: 8/3/2026, 8:14:34 PM
1class Solution:
2    def findLongestChain(self, pairs: List[List[int]]) -> int:
3        pairs.sort(key=lambda x:x[1])
4        res=1
5        prev=pairs[0][1]
6        for start,end in pairs[1:]:
7            if start>prev:
8                prev=end
9                res+=1
10        return res