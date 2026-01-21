# Last updated: 1/21/2026, 10:27:46 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        R=len(nums)-1
4        n=len(nums)
5        L=0
6        idx=n-1
7        res = [0]*n
8        while L<=R:
9            if abs(nums[L])<abs(nums[R]):
10                res[idx] = nums[R]*nums[R]
11                R-=1
12            else:
13                res[idx]=nums[L]*nums[L]
14                L+=1
15            idx-=1
16        return res