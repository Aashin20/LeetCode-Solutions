class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()
        n = len(nums)

        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2 
                else:
                    i += 1
            return count >= p

        left, right = 0, int(1e9)
        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left