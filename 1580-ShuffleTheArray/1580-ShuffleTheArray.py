# Last updated: 6/14/2025, 10:32:38 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res
        