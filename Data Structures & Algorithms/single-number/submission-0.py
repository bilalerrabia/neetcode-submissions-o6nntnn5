class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = {nums.count(v): v for v in nums}
        return mydict[1]