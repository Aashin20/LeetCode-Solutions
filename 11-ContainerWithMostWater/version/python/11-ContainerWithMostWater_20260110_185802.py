# Last updated: 1/10/2026, 6:58:02 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n = len(height)
4        L=0
5        R=n-1
6        high = 0
7        while L<R:
8            high = max(min(height[L],height[R])*(R-L),high)
9            if height[L]<height[R]:
10                L+=1
11            else:
12                R-=1
13        return high