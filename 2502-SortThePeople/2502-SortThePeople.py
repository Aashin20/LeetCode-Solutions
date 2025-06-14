# Last updated: 6/14/2025, 10:32:14 PM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(heights)), key= lambda i: -heights[i])]