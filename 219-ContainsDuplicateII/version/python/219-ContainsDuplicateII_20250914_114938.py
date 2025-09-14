# Last updated: 9/14/2025, 11:49:38 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                if abs(indices[nums[i]]-i)<=k:
                    return True
            
            indices[nums[i]]=i
        return False