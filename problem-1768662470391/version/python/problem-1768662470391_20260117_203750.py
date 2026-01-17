# Last updated: 1/17/2026, 8:37:50 PM
1class Solution:
2    def minOperations(self, nums: List[int], target: List[int]) -> int:
3        operations = set()
4        for i in range(len(nums)):
5            if nums[i]!=target[i]:
6                operations.add(nums[i])
7        return len(operations)