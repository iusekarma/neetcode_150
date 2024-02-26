class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = nums[0]
        for i in nums[1:]:
            out ^= i
        return out