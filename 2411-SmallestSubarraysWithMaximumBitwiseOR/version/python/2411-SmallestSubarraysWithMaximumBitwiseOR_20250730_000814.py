# Last updated: 7/30/2025, 12:08:14 AM
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last_seen = [0] * 30
        res = [1] * n
        for i in range(n - 1, -1, -1):
            for bit in range(30):
                if (nums[i] & (1 << bit)) > 0:
                    last_seen[bit] = i
                res[i] = max(res[i], last_seen[bit] - i + 1)
        return res