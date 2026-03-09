# Last updated: 3/9/2026, 11:16:43 PM
1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        res = defaultdict(list)
5        for s in strs:
6            count = [0]*26
7            for c in s:
8                count[ord(c)-ord('a')]+=1
9            res[tuple(count)].append(s)
10        return list(res.values())