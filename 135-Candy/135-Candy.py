# Last updated: 6/14/2025, 10:33:49 PM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        result=[1]*n
        for i in range(1,n):
            if  ratings[i]>ratings[i-1]:
                result[i]=result[i-1]+1
            else:
                continue
        
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1] :
                result[j]=max(result[j],result[j+1]+1)
            else:
                continue
        return sum(result)
            