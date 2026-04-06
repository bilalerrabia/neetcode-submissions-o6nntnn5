class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num = min(nums)
        num_max = max(nums)
        for i in range(1, num_max + 2):
            if i not in nums:
                return i
        return 1
        