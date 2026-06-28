# Last updated: 6/28/2026, 10:38:06 AM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        count=[0,0,0]
7        for color in nums:
8            count[color]+=1
9        R,W,B=count
10        nums[:R]=[0]*R
11        nums[R:R+W]=[1]*W
12        nums[R+W::]=[2]*B