class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if i in s:
                continue
            else:
                a.append(i)
        return a

