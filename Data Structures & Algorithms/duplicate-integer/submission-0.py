class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        if len(nums) == len(new_nums):
            return False
        return True