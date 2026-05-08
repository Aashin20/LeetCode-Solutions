# Last updated: 5/8/2026, 11:59:34 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        if n==2:
7            return max(nums[0],nums[1])
8        ans=[0]*n
9        ans[0]=nums[0]
10        ans[1]=max(nums[0],nums[1])
11        for i in range(2,n):
12            ans[i]=max(ans[i-1],nums[i]+ans[i-2])
13            
14        return ans[-1]