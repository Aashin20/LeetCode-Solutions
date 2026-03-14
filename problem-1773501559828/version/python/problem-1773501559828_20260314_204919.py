# Last updated: 3/14/2026, 8:49:19 PM
1from collections import Counter
2class Solution:
3    def firstUniqueEven(self, nums: list[int]) -> int:
4        count = Counter(nums)
5        for k,v in count.items():
6            if v==1 and k%2==0:
7                return k
8        return -1