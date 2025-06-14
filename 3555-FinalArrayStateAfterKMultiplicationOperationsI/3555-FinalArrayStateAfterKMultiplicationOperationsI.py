# Last updated: 6/14/2025, 10:31:46 PM
class Solution:
    # Time Complexity: O(n * k)
    # Space Complexity: O(1)
    def getFinalState0(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            idx = min(range(len(nums)), key=lambda x: nums[x])
            nums[idx] *= multiplier
        return nums

    # Time Complexity: O(n + k * log(n))
    # Space Complexity: O(n)
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        pq = [(x, i) for i, x in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            nums[pq[0][1]] = pq[0][0] * multiplier
            heapreplace(pq, (pq[0][0] * multiplier, pq[0][1]))

        return nums