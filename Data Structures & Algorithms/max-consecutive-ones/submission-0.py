class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        for i in range(len(nums)):
            max_tmp = 0
            if nums[i] == 1:
                while i < len(nums) and nums[i] == 1:
                    max_tmp += 1
                    i += 1
                if max_tmp > max_:
                    max_ = max_tmp
            if i == len(nums):
                return max_
            if nums[i] == 0:
                while i < len(nums) and nums[i] == 0:
                    i += 1
        return max_
                
        