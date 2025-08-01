# Last updated: 8/1/2025, 7:40:15 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        hashmap={')':'(',']':'[','}':'{'}
        for i in s:
            if i not in hashmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped!=hashmap[i]:
                        return False
        return not stk