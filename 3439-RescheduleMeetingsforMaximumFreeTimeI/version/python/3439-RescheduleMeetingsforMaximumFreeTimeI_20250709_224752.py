# Last updated: 7/9/2025, 10:47:52 PM
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        count = len(startTime)
        prefixSum = [0] * (count + 1)
        maxFree = 0

        for i in range(count):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])

        for i in range(k - 1, count):
            occupied = prefixSum[i + 1] - prefixSum[i - k + 1]
            windowEnd = eventTime if i == count - 1 else startTime[i + 1]
            windowStart = 0 if i == k - 1 else endTime[i - k]
            freeTime = windowEnd - windowStart - occupied
            maxFree = max(maxFree, freeTime)

        return maxFree