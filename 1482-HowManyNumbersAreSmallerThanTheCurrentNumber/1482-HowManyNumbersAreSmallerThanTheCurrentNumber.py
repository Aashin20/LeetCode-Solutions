# Last updated: 6/14/2025, 10:32:40 PM
from itertools import accumulate
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102  
        for number in nums:
            count[number + 1] += 1
        sum_count = list(accumulate(count))
        return [sum_count[number] for number in nums]