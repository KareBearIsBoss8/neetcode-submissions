class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        res = 0

        for i in nums:
            if i-1 in nums_set:
                continue
            curr = i
            streak = 0
            while curr in nums:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res