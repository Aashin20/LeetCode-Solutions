# Last updated: 6/14/2025, 10:33:43 PM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            index = (columnNumber - 1) % 26
            result = chr(index + ord('A')) + result
            columnNumber = (columnNumber - 1) // 26
        return result