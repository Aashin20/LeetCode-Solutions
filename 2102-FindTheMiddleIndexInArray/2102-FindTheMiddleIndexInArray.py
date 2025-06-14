# Last updated: 6/14/2025, 10:32:25 PM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:               
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            if leftSum == rightSum - nums[i]:
                return i

            leftSum += nums[i]
            rightSum -= nums[i]

        return -1