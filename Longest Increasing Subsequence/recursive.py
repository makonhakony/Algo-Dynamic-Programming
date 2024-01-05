def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i, prev):
            if i == len(nums):
                return 0
            taken = 0
            if nums[i] > prev:
                taken = 1 + dp(i+1, nums[i])
            not_taken = dp(i+1, prev)
            return max(taken, not_taken)
        return dp(0, float('-inf'))