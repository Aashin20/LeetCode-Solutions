from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if counter[i]==0:
                a.append(i)
            else:
                continue
        return a

        