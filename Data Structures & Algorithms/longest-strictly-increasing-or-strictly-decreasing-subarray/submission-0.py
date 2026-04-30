class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_flag = 0
        global_longest = 1
        current_longest = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                # increasing
                if increasing_flag > 0:
                    current_longest += 1
                else:
                    current_longest = 2
                    increasing_flag = 1
            elif nums[i - 1] > nums[i]:
                # decreasing
                if increasing_flag < 0:
                    current_longest += 1
                else:
                    current_longest = 2
                    increasing_flag = -1
            else:
                current_longest = 1
                increasing_flag = 0
            global_longest = max(global_longest, current_longest)
        return global_longest