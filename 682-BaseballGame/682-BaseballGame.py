# Last updated: 6/14/2025, 10:33:02 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in operations:
            if i == "D":
                stk.append(int(stk[-1])*2)
            elif i == "C":
                stk.pop()
            elif i == "+":
                stk.append(int(stk[-1])+int(stk[-2]))
            else:
                stk.append(int(i))
        return sum(stk)