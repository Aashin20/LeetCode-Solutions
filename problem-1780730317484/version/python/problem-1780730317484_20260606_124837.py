# Last updated: 6/6/2026, 12:48:37 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered_list = sorted([(p, s) for p, s in zip(position, speed)], key=lambda x: x[0], reverse=True)
        
        stack = list()
        for p, s in ordered_list:
            req_time = (target - p) / s

            if not stack or stack[-1] < req_time:
                stack.append(req_time)
        
        return len(stack)