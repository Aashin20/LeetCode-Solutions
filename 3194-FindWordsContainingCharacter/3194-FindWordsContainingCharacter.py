# Last updated: 6/14/2025, 10:31:57 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
                continue
            else:
                continue
        return a
        