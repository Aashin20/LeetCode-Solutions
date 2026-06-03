# Last updated: 6/3/2026, 6:02:18 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        maxL=0
4        maxR=0
5        hL=[maxL]*len(height)
6        hR=[maxR]*len(height)
7        n=len(height)
8        for i in range(n):
9            j=-i-1
10            hL[i]=maxL
11            hR[j]=maxR
12            maxL=max(maxL,height[i])
13            maxR=max(maxR,height[j])
14        
15        summ=0
16        for i in range(n):
17            pot=min(hL[i],hR[i])
18            summ+=max(0,pot-height[i])
19        return summ