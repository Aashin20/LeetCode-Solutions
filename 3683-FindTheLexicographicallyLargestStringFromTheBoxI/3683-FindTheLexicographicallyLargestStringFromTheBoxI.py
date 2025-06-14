# Last updated: 6/14/2025, 10:31:44 PM
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        else:
            n = len(word)
            res = ""
            for i in range(n):
                res = max(res, word[i: min(i+n-numFriends+1,n)])
            return res
