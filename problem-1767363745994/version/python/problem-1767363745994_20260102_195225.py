# Last updated: 1/2/2026, 7:52:25 PM
1from collections import Counter
2class Solution:
3    def repeatedNTimes(self, nums: List[int]) -> int:
4        size = len(nums)//2
5        count = Counter(nums)
6        for i in count:
7            if count[i]==size:
8                return i
9            else:
10                continue