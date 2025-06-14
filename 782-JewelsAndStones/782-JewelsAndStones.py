# Last updated: 6/14/2025, 10:32:57 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count
        