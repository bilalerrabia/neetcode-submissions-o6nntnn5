class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nums = nums[-1:] + nums[0:-1]
            print(nums)
            if nums == sorted(nums):
                return True
        return False