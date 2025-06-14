# Last updated: 6/14/2025, 10:33:19 PM
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        top_k = counter.most_common(k)
        return list(map(lambda x: x[0], top_k))