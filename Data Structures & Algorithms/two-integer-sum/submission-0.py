class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        for i, j in enumerate(nums):
            k = target - j

            if k in diff:
                return [diff[k], i]
            
            diff[j] = i
        return []