# Last updated: 6/14/2025, 10:32:37 PM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1 
            else:
                d[i] = 1 
        for key, val in d.items():
            if val == 1:
                unique.append(key)
        return sum(unique)