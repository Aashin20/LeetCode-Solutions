# Last updated: 8/1/2025, 12:02:06 AM
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)