# Last updated: 6/3/2026, 10:00:08 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        nums=numbers
4        n=len(nums)
5        L=0
6        R=n-1
7        while L<R:
8            summ=nums[L]+nums[R]
9            if summ==target:
10                return [L+1,R+1]
11            elif summ<target:
12                L+=1
13            else: R-=1
14