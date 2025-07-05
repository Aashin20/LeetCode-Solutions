# Last updated: 7/5/2025, 11:20:47 PM
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        keyy=-1
        nums = Counter(arr)
        for key,val in nums.items():
            if key==val:
                keyy=max(keyy,key)
        return keyy
        