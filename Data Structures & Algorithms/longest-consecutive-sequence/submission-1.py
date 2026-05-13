class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        res = 0

        for i in nums:
            if i-1 not in nums_set:
                streak = 1
                while i + streak in nums:
                    streak += 1
                res = max(res, streak)
        return res