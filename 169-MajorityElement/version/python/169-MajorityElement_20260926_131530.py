# Last updated: 9/26/2026, 1:15:30 PM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: list[int]) -> int:
4        count=Counter(nums)
5        return max(count,key=count.get)
6        
7                