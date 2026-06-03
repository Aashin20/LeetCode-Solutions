# Last updated: 6/3/2026, 8:14:39 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        L=0
4        R=len(height)-1
5        maxx=0
6        while L<R:
7            maxx=max(maxx,min(height[L],height[R])*(R-L))
8            if height[L]<height[R]:
9                L+=1
10            else:
11                R-=1
12        return maxx