# Last updated: 7/2/2025, 8:54:05 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1 
        count=0
        sum=0
        for num in nums:
            sum+=num
            if (sum-k) in prefix:
                count+=prefix[sum-k]
            prefix[sum]+=1

        return count
        