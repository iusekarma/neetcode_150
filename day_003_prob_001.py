class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_n = {}
        for i in range(len(nums)):
            f = target-nums[i]
            if f in d_n and i != d_n[f]:
                return d_n[f],i
            else:
                d_n[nums[i]] = i